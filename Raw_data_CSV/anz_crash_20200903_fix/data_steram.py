from Write_Data_to_db import insert_car_crash
db_path = "Car_crash.db"
import pandas as pd

# Load CSV files, dropping unnecessary columns
casualties = pd.read_csv("Casualties.csv",low_memory=False)
crash = pd.read_csv("Crash2.csv",low_memory=False)
description = pd.read_csv("Description.csv",low_memory=False)
vehicles = pd.read_csv("Vehicles.csv",low_memory=False)
date_time = pd.read_csv("DateTime.csv",low_memory=False)

"""try:
    for x in range(1,2):#len(date_time)):
        day_of_week_hour_data = date_time.loc[crash["date_time_id"].iloc[x] == date_time['date_time_id'], ['day_of_week', 'hour']].copy()
        description_data = description.loc[crash["description_id"].iloc[x] == description["description_id"],["severity","speed_limit",'midblock','intersection','road_position_horizontal','road_position_vertical','road_sealed',"road_wet",'weather','crash_type','lighting','traffic_controls',]].copy()
        casualties_data = casualties.loc[crash["casualties_id"].iloc[x] == casualties["casualties_id"],['fatalities','serious_injuries','minor_injuries']].copy()
        vehicles_raw_data = vehicles.loc[crash["vehicles_id"].iloc[x] == vehicles['vehicles_id'],['car_sedan','car_utility','car_van','car_4x4','car_station_wagon','motor_cycle','truck_small','truck_large','bus','taxi','bicycle','scooter','pedestrian','inanimate','vehicle_other']].copy()
        vehicles_data_sum = vehicles_raw_data.iloc[0].sum(axis=0)
        vehicles_data = vehicles_raw_data.loc[:, (vehicles_raw_data != 0).any(axis=0)]
        l = list(vehicles_data)
        s = ",".join(l)

        df_vehicles = pd.DataFrame({"Type_of_vehicles" : [s],
                                    "Total_of_vehicles" : [vehicles_data_sum]
                                })

        sql_data = day_of_week_hour_data.join([description_data,casualties_data,df_vehicles])

        print(casualties_data)

        print(sql_data)

        for _, row in sql_data.iterrows():
            insert_car_crash(
                db_path=db_path,
                day_of_week=int(row["day_of_week"]),
                hour_of_crash=float(row["hour"]),
                severity=row["severity"],
                speed_limit=int(row["speed_limit"]),
                midlock=bool(row["midblock"]),
                intersection=bool(row["intersection"]),
                road_position_horizontal=row["road_position_horizontal"],
                road_position_vertical=row["road_position_vertical"],
                road_slope=bool(row["road_sealed"]),
                road_wet=bool(row["road_wet"]),
                weather=row["weather"],
                crash_type=row["crash_type"],
                lighting=row["lighting"],
                traffic_controls=row["traffic_controls"],
                fatalities=int(row["fatalities"]),
                serious_injuries=int(row["serious_injuries"]),
                minor_injuries=int(row["minor_injuries"]),
                type_of_vehicles=row["Type_of_vehicles"],
                total_of_vehicles=int(row["Total_of_vehicles"])
            )
except Exception as e:
    print(e)
except MemoryError:
    print(MemoryError)
"""

marage = pd.merge(left=crash,right=description,left_on="description_id",right_on="description_id",how="left")
marage = pd.merge(left=marage,right=casualties,left_on="casualties_id",right_on="casualties_id",how='left')
#marage = pd.merge(left=marage,right=vehicles,left_on="vehicles_id",right_on="vehicles_id",how='left')

marage = pd.merge(left=marage,right=date_time,left_on="date_time_id",right_on="date_time_id",how="left")
marage = pd.merge(
    left=marage,
    right=vehicles,
    left_on="vehicles_id",
    right_on="vehicles_id",
    how='left',
    suffixes=('_marage', '_vehicles')
)

#print(marage.iloc[1123982])
try:
    for _, row in marage.iloc[1123982:].iterrows():
        insert_car_crash(
            db_path=db_path,
            day_of_week=row["day_of_week"],
            hour_of_crash=row["hour"],
            severity=row["severity"],
            speed_limit=row["speed_limit"],
            midlock=row["midblock"],
            intersection=row["intersection"],
            road_position_horizontal=row["road_position_horizontal"],
            road_position_vertical=row["road_position_vertical"],
            road_slope=row["road_sealed"],  # Assuming 'road_slope' should still be included if available
            road_wet=row["road_wet"],
            weather=row["weather"],
            crash_type=row["crash_type"],
            lighting=row["lighting"],
            traffic_controls=row["traffic_controls"],
            fatalities=row["fatalities"],
            serious_injuries=row["serious_injuries"],
            minor_injuries=row["minor_injuries"],
            type_of_vehicles = ", ".join(row["vehicle_other"]) if isinstance(row["vehicle_other"], (list, tuple)) and row["vehicle_other"] else None,  # Assuming 'vehicle_other' should be used for this
            total_of_vehicles=row["vehicles_id"]  # Adjusting this based on your input
        )
except NotImplementedError as intse:
    print(intse)
except Exception as e:
    print(e)
