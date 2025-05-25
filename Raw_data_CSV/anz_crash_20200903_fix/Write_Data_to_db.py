import sqlite3

def insert_car_crash(db_path, day_of_week, hour_of_crash, severity, speed_limit, midlock=False, intersection=False, 
                     road_position_horizontal=None, road_position_vertical=None, road_slope=False, road_wet=False,
                     weather=None, crash_type=None, lighting=None, traffic_controls=None, 
                     fatalities=0, serious_injuries=0, minor_injuries=0, type_of_vehicles=None, total_of_vehicles=None):
    """
    Inserts a record into the Car_crash table.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - day_of_week (int): Day of the week (e.g., 1 for Monday).
    - hour_of_crash (float): Hour of the crash (e.g., 13.5 for 1:30 PM).
    - severity (str): Severity of the crash.
    - speed_limit (int): Speed limit at the location.
    - midlock (bool): Whether midlock was involved.
    - intersection (bool): Whether the crash occurred at an intersection.
    - road_position_horizontal (str): Horizontal road position.
    - road_position_vertical (str): Vertical road position.
    - road_slope (bool): Whether the road had a slope.
    - road_wet (bool): Whether the road was wet.
    - weather (str): Weather conditions.
    - crash_type (str): Type of crash.
    - lighting (str): Lighting conditions.
    - traffic_controls (str): Traffic control measures.
    - fatalities (int): Number of fatalities.
    - serious_injuries (int): Number of serious injuries.
    - minor_injuries (int): Number of minor injuries.
    - type_of_vehicles (str): Type of vehicles involved.
    - total_of_vehicles (int): Total number of vehicles involved.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL insert statement
        sql = '''
        INSERT INTO Car_crash (
            Day_of_week, Hour_of_crash, Severity, Speed_limit, Midlock, Intersection,
            Road_position_horizontal, Road_position_vertical, Road_slope, Road_wet,
            Weather, Crash_type, Lighting, Traffic_controls, Fatalities, Serious_injuries,
            Minor_injuries, Type_of_vehicles, Total_of_vehicles
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

        # Execute the insert statement
        cursor.execute(sql, (
            day_of_week, hour_of_crash, severity, speed_limit, midlock, intersection,
            road_position_horizontal, road_position_vertical, road_slope, road_wet,
            weather, crash_type, lighting, traffic_controls, fatalities, serious_injuries,
            minor_injuries, type_of_vehicles, total_of_vehicles
        ))

        # Commit the transaction and close the connection
        conn.commit()
        print("Data inserted successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()