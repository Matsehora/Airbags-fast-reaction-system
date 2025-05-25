import requests
from datetime import datetime,timedelta

def get_decoded_weather(lat, lon,date):
    # Define weather code mappings
    weather_code_map = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light intensity",
        53: "Drizzle: Moderate intensity",
        55: "Drizzle: Dense intensity",
        56: "Freezing drizzle: Light",
        57: "Freezing drizzle: Dense",
        61: "Rain: Slight intensity",
        63: "Rain: Moderate intensity",
        65: "Rain: Heavy intensity",
        66: "Freezing rain: Light",
        67: "Freezing rain: Heavy",
        71: "Snow fall: Slight intensity",
        73: "Snow fall: Moderate intensity",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers: Slight",
        86: "Snow showers: Heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with hail: Slight",
        99: "Thunderstorm with hail: Heavy",
    }
    
    # Open-Meteo API endpoint and parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "weathercode",
        "timezone": "auto",
        "start_date": date,
        "end_date": date,
    }
    
    # Make the API call
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": f"Failed to fetch weather data: {response.text}"}
    
    # Parse the API response
    data = response.json()
    hourly_times = data.get("hourly", {}).get("time", [])
    hourly_codes = data.get("hourly", {}).get("weathercode", [])
    
    # Decode weather codes into descriptions
    weather_dict = {}
    for i in range(len(hourly_times)):
        time = datetime.fromisoformat(hourly_times[i]).strftime("%H:%M")
        code = hourly_codes[i]
        weather_dict[time] = weather_code_map.get(code, "Unknown weather condition")
    
    return weather_dict

def get_decoded_weather_on_road_rn(lat, lon):
    """
    Take latitude and longitude 
    
    eturns two values: 
        1. Weather condition, if form of string 
        2. Boolean for - if road is wet? True - road is wet, False - road is not wet

    """
    try:
        road_wet = False

        LIST_FOR_ALL_DAY = ["Thunderstorm: Slight or moderate","Thunderstorm with hail: Heavy",
                            "Drizzle: Moderate intensity","Drizzle: Dense intensity","Freezing drizzle: Dense","Rain: Moderate intensity"
                            "Rain: Heavy intensity","Freezing rain: Heavy","Rain showers: Moderate","Rain showers: Violent"]

        weather_today = get_decoded_weather(lat, lon,datetime.now().strftime("%Y-%m-%d"))
        yesterday = datetime.now() - timedelta(days=1)
        weather_yesterday = get_decoded_weather(lat, lon,yesterday.strftime("%Y-%m-%d")) 

        Rain_yesterday = any(any(substring in value for substring in LIST_FOR_ALL_DAY) for value in weather_yesterday.values())
        Rain_today = any(any(substring in value for substring in LIST_FOR_ALL_DAY) for value in weather_today.values())
        hour_now = datetime.now().hour

        Rain_not_so_long_ago = False
                

        for x in range(hour_now-2,hour_now+2):
            value = weather_today.get(str(x)+":00")
            if "rain" in value.lower():
                Rain_not_so_long_ago = True
            elif "Thunderstorm" in value:
                Rain_not_so_long_ago = True
            elif "drizzle" in value.lower():
                Rain_not_so_long_ago = True

        if Rain_yesterday or Rain_today or Rain_not_so_long_ago:
            road_wet = True

        return weather_today.get(str(hour_now)+":00"),road_wet
    except Exception as e:
        print("EROOR",e)
        return "Overcast",False
    



# Example usage
latitude = 37.7749  # Example: San Francisco
longitude = -122.4194
'''weather_today = get_decoded_weather(latitude, longitude,datetime.now().strftime("%Y-%m-%d"))
yesterday = datetime.now() - timedelta(days=1)
weather_yestoday = get_decoded_weather(latitude, longitude,yesterday.strftime("%Y-%m-%d")) 

print(weather_today)
print(weather_yestoday)
'''

print(get_decoded_weather_on_road_rn(latitude,longitude))