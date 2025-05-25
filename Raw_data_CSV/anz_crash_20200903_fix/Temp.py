import sqlite3
import pandas as pd
import numpy as np

#date_time = pd.read_csv("DateTime.csv",low_memory=False)
#crash = pd.read_csv("Crash2.csv",low_memory=False)
#marage = pd.merge(left=crash,right=date_time,left_on="date_time_id",right_on="date_time_id",how="left")
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("Car_crash.db")

column_names = [
    "Day_of_week",
    "Hour_of_crash",
    "Severity",
    "Speed_limit",
    "Midlock",
    "Intersection",
    "Road_position_horizontal",
    "Road_position_vertical",
    "Road_slope",
    "Road_wet",
    "Weather",
    "Crash_type",
    "Lighting",
    "Traffic_controls",
]



# Create a cursor object to interact with the database
cursor = conn.cursor()
#Lighting = 'darkness_not_lit' OR Lighting IS NULL OR Lighting = 'unknown') AND Road_wet = 0 AND (Weather = 'fine' OR Weather IS NULL OR Weather = 'unknown') AND Intersection = 0 AND Midlock IS 0
cursor.execute("SELECT DISTINCT Speed_limit FROM Car_crash")
#cursor.execute("SELECT * FROM Car_crash WHERE Midlock IS 1")

#cursor.execute("SELECT * FROM Car_crash WHERE (Lighting = 'darkness_not_lit' OR Lighting IS NULL OR Lighting = 'unknown') AND Road_wet = 0 AND (Weather = 'fine' OR Weather IS NULL OR Weather = 'unknown') AND Intersection = 0 AND Midlock IS 0")
rows = cursor.fetchall()
print(rows)

conn.close()


#a = "SELECT DISTINCT {asx} FROM Car_crash"
#count_query = "SELECT COUNT(*) FROM Car_crash WHERE {asx} = ?"
#with open(r"C:\Users\User\Desktop\Дипломна робота\data_form_steps.txt", 'w') as f:
    #for x in column_names:
        # Execute a SELECT query to get distinct values
        #cursor.execute(a.format(asx=x))
        #rows = cursor.fetchall()

        # Write column name
        #f.write(x + "\n")

        #for row in rows:
            #value = row[0]  # Extract value
            #formatted_row = str(value)

            # Execute the count query for the current value
            #cursor.execute(count_query.format(asx=x), (value,))
            #count = cursor.fetchone()[0]  # Fetch count result

            # Write value and count
            #f.write(f"{formatted_row}: {count}\n")

        #f.write("\n")
        #print(len(rows))
