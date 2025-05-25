from geopy.distance import geodesic

def is_within_2m(coord1, coord2):
    """
    Check if coord2 is within 2 meters of coord1.
    
    :param coord1: Tuple (longitude, latitude) of first coordinate
    :param coord2: Tuple (longitude, latitude) of second coordinate
    :return: True if within 2 meters, False otherwise
    """
    distance = geodesic((coord1[1], coord1[0]), (coord2[1], coord2[0])).meters
    return distance <= 2
