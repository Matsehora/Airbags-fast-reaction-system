import requests
from datetime import datetime, timedelta, timezone

def get_lighting_condition_on_road(latitude, longitude, hour):
    """
    Determine lighting condition for given latitude, longitude, and hour.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        hour (str): Hour in HH:MM format, UTC timezone.

    Returns:
        tuple: One of ('daylight',), ('darkness_not_lit',), ('darkness_lit',), ('dawn_dusk',), or ('other',).
    """
    try:
        # Query Open-Meteo API for sunrise and sunset times
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "daily": "sunrise,sunset",
                "timezone": "UTC",
            },
        )

        if response.status_code != 200:
            return ('other',)

        data = response.json()
        sunrise = data['daily']['sunrise'][0]  # Sunrise time (UTC)
        sunset = data['daily']['sunset'][0]    # Sunset time (UTC)

        # Convert hour to a datetime object
        current_time = datetime.strptime(hour, "%H:%M").replace(tzinfo=timezone.utc)
        sunrise_time = datetime.fromisoformat(sunrise).replace(tzinfo=timezone.utc)
        sunset_time = datetime.fromisoformat(sunset).replace(tzinfo=timezone.utc)

        # Define dawn and dusk times (1 hour before/after sunrise/sunset)
        dawn_start = sunrise_time - timedelta(hours=1)
        dawn_end = sunrise_time
        dusk_start = sunset_time
        dusk_end = sunset_time + timedelta(hours=1)

        # Determine lighting condition
        if dawn_start <= current_time < dawn_end or dusk_start <= current_time < dusk_end:
            return 'dawn_dusk'
        elif sunrise_time <= current_time < sunset_time:
            return 'daylight'
        elif current_time < dawn_start or current_time >= dusk_end:
            return 'darkness_not_lit' # Assume not lit by default
        else:
            return 'other'

    except Exception as e:
        print(f"Error: {e}")
        return 'other'

"""# Example usage
latitude = 52.52  # Berlin
longitude = 13.41
hour = "20:30"  # 8:30 PM UTC

lighting_condition = get_lighting_condition_on_road(latitude, longitude, hour)
print(lighting_condition)
"""