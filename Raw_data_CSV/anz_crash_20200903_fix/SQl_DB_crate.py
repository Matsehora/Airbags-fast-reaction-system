import sqlite3

coon = sqlite3.connect("Car_crash.db")

cursor = coon.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Car_crash (
                Car_crash_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Day_of_week INT,
                Hour_of_crash FLOAT,
                Severity TEXT,
                Speed_limit INT,
                Midlock BOOLEAN DEFAULT False,
                Intersection BOOLEAN DEFAULT False,
                Road_position_horizontal TEXT,
                Road_position_vertical TEXT,
                Road_slope BOOLEAN DEFAULT False,
                Road_wet BOOLEAN DEFAULT False,
                Weather TEXT,
                Crash_type TEXT,
                Lighting TEXT,
                Traffic_controls TEXT,
                Fatalities INT DEFAULT 0,
                Serious_injuries INT DEFAULT 0,
                Minor_injuries INT DEFAULT 0,
                Type_of_vehicles TEXT,
                Total_of_vehicles INT
);

""")

coon.commit()
coon.close()

print("DB was created")