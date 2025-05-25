import openrouteservice
import osmnx as ox
import networkx as nx
import math
from dotenv import load_dotenv
import os
from shapely.geometry import LineString, Point
from math import isclose



def get_route_details_with_coords(start_point, end_point, ors_api_key):
    """
    Get route details with event descriptions and coordinates adjusted 5m before the event.
    Includes specific turn and intersection directions.

    Args:
        start_point (tuple): Coordinates of the starting point (longitude, latitude).
        end_point (tuple): Coordinates of the ending point (longitude, latitude).
        ors_api_key (str): OpenRouteService API key.

    Returns:
        list: Description of each route segment (e.g., "straight road", "midblock", "intersection", "turn").
        list: Coordinates (longitude, latitude) of when events happen, adjusted by 5m before the event.
    """
    def adjust_coordinates(coord1, coord2, distance_m):

        """
        Adjust coordinates `coord1` towards `coord2` by a given distance in meters.

        Args:
            coord1 (tuple): Starting coordinate (longitude, latitude).
            coord2 (tuple): Target coordinate (longitude, latitude).
            distance_m (float): Distance in meters to adjust.

        Returns:
            tuple: Adjusted coordinate (longitude, latitude).
        """
        # Approximate Earth's radius in meters
        R = 6371000

        # Convert degrees to radians
        lon1, lat1 = math.radians(coord1[0]), math.radians(coord1[1])
        lon2, lat2 = math.radians(coord2[0]), math.radians(coord2[1])

        # Compute bearing from coord1 to coord2
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        bearing = math.atan2(
            math.sin(dlon) * math.cos(lat2),
            math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        )

        # Adjust distance to radians
        adjusted_distance = distance_m / R

        # Calculate the adjusted coordinates
        lat_adjusted = math.asin(
            math.sin(lat1) * math.cos(adjusted_distance) +
            math.cos(lat1) * math.sin(adjusted_distance) * math.cos(bearing)
        )
        lon_adjusted = lon1 + math.atan2(
            math.sin(bearing) * math.sin(adjusted_distance) * math.cos(lat1),
            math.cos(adjusted_distance) - math.sin(lat1) * math.sin(lat_adjusted)
        )

        # Convert radians back to degrees
        return (math.degrees(lon_adjusted), math.degrees(lat_adjusted))

    # Функція для перевірки, чи координати підходять між двома іншими
    def is_between(coord, coord1, coord2):
        return coord1 <= coord <= coord2 or coord2 <= coord <= coord1

    # Вставка верхнього списку в нижній
    def merge_coordinates(upper_list, lower_list):
        merged_list = lower_list[:]  # Копіюємо нижній список
        for coord in upper_list:
            inserted = False
            for i in range(len(merged_list) - 1):
                # Якщо координата підходить між двома іншими, вставляємо її
                if is_between(coord, merged_list[i], merged_list[i + 1]):
                    merged_list.insert(i + 1, coord)
                    events.insert(i + 1, "mid-lock")
                    inserted = True
                    break
            '''if not inserted:
                # Якщо координата не підходить ніде, додаємо її в кінець
                merged_list.append(coord)'''
        return merged_list

    # Initialize ORS client
    client = openrouteservice.Client(key=ors_api_key)

    # Request directions from ORS
    route = client.directions(
        coordinates=[start_point, end_point],
        profile='driving-car',
        format='geojson'
    )

    # Extract route geometry and steps
    geometry = route['features'][0]['geometry']['coordinates']
    steps = route['features'][0]['properties']['segments'][0]['steps']
    print(steps)

    # Load OpenStreetMap graph for road data
    G = ox.graph_from_point(start_point[::-1], dist=2000, network_type='drive')  # Buffer around the start point
    route_nodes = ox.nearest_nodes(G, [coord[0] for coord in geometry], [coord[1] for coord in geometry])

    
    
    route_line = LineString([(coord[0], coord[1]) for coord in geometry])

    # Find mid-block crossings
    mid_block_crossings = []

    # Extract all crossings (nodes with `highway=crossing`)
    for node, data in G.nodes(data=True):
        if data.get('highway') == 'crossing':  # Check if node is a pedestrian crossing
            crossing_coords = (data['x'], data['y'])
            crossing_point = Point(crossing_coords)
            
            # Check if crossing is along the route (within buffer distance)
            if route_line.buffer(2).contains(crossing_point):  # 10 meters buffer
                # Check if the crossing is mid-block (not at an intersection)
                neighbors = list(G.neighbors(node))
                if len(neighbors) <= 2:  # Not an intersection if 2 or fewer connected edges
                    mid_block_crossings.append(crossing_coords)
    
    # Analyze route
    events = []  # List to store segment types
    event_coords = []  # List to store adjusted coordinates of events


    for step in steps:
            
        print(step)
        #instruction = step['instruction'].lower()
        type_in_steps = step['type']

        if type_in_steps in [6,11,12,13]:
            events.append("straight road")
        elif type_in_steps in [0,2,4]:
             events.append("turn left")
        elif type_in_steps in [1,3,5]:
            events.append("turn right")
        elif type_in_steps in [7,8]:
            events.append("roundabout")
        elif type_in_steps == 9:
            events.append("u-turn")

        
        # Adjust the event coordinate 5m before the event
        coord_before_event = adjust_coordinates(
            geometry[step['way_points'][1] - 1],
            geometry[step['way_points'][1]],
            3
        )

        
        event_coords.append(coord_before_event)

    adjusted_mid_block_crossings = []

    for crossing_coords in mid_block_crossings:
        # Reference point for direction (e.g., a nearby route node or any other point)
        # Here, we use the first route node as an example
        reference_point = geometry[0]  # First coordinate from the route geometry
        
        # Adjust crossing by 3 meter towards the reference point
        adjusted_coords = adjust_coordinates(crossing_coords, reference_point, distance_m=3)
        
        # Store the adjusted crossing coordinates
        adjusted_mid_block_crossings.append(adjusted_coords)

    final_coords_list = merge_coordinates(adjusted_mid_block_crossings, event_coords)
 
    return events, final_coords_list

# Example usage
# uses long lat 
start = (8.8078, 53.0758)  # Bremen city center
end = ( 9.72970425846439,52.37549667131688)    # Oldenburg city center

load_dotenv("API_keys.env")
api_key = os.getenv("openrouteservice_api_key")

route_events, event_coords = get_route_details_with_coords(start, end, api_key)

print("Route Events:", route_events)
print("Event Coordinates:", event_coords)
