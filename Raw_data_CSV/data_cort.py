import pandas as pd

df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv')

df = df.get("casualties","fatalities","serious_injuries","minor_injuries")



print(df.to_string()) 