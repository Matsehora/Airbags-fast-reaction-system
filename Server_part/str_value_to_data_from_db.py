import datetime
from Data_from_db_using_condition import get_data_from_db
from get_lighting_condition import get_lighting_condition_on_road
from get_the_weather import get_decoded_weather_on_road_rn
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging
logging.basicConfig(
    filename="db_call_processing_code.log",  # Log file name
    level=logging.DEBUG,  # Log ALL levels (DEBUG and above)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def str_to_db_return_all_values(latitude, longitude,value:str=None):
    """
   Function for getting data from database on parametres latitude, longitude 
   value is presenting value direction that car will need to take
    
    """

   


    def call_to_db(day_of_week_call:str,hour_of_crash_call:str,Lighting_Condition_call:str,Road_Weat_Condition_call,Weather_Condition_cal,Additional_Values_for_call = ''):
        try:
            ultimate_call_to_omnissiah = day_of_week_call + hour_of_crash_call + Lighting_Condition_call + Road_Weat_Condition_call + Weather_Condition_cal + Additional_Values_for_call
            print(ultimate_call_to_omnissiah)
            return_data_form_db = get_data_from_db(ultimate_call_to_omnissiah)
            logging.debug("First run in call_to_db() was successful")
            logging.debug(f"DB call was {ultimate_call_to_omnissiah}")

            if (return_data_form_db is None) or (len(return_data_form_db) < 100):
                logging.debug("return_data_form_db was None or data in it was less then 100 in first run")
                ultimate_call_to_omnissiah = day_of_week_call + Lighting_Condition_call + Road_Weat_Condition_call + Weather_Condition_cal + Additional_Values_for_call
                return_data_form_db =  get_data_from_db(ultimate_call_to_omnissiah)
                logging.debug("Second run in call_to_db() was successful")
                logging.debug(f"DB call was {ultimate_call_to_omnissiah}")
            
                if (return_data_form_db is None) or (len(return_data_form_db) < 100):
                    ("return_data_form_db was None or data in it was less then 100 in second run")
                    ultimate_call_to_omnissiah = Lighting_Condition_call[4:] + Road_Weat_Condition_call + Weather_Condition_cal + Additional_Values_for_call
                    print(ultimate_call_to_omnissiah)
                    return_data_form_db =  get_data_from_db(ultimate_call_to_omnissiah)
                    logging.debug("Third run in call_to_db() was successful")
                    logging.debug(f"DB call was {ultimate_call_to_omnissiah}")

            logging.debug(f"Was exstrected {len(return_data_form_db)} rows from db")
            return return_data_form_db
        except Exception as e:
            logging.error(f"Error in call_to_db(): {e}")
            return("Database request error")

    try:
        day_of_the_week = datetime.datetime.today().weekday()+1
        Day_of_week_call = " (Day_of_week = {x1} OR Day_of_week IS NULL)".format(x1=day_of_the_week)
        logging.debug(f"Day_of_week_call = {Day_of_week_call}, no Errors")
    except Exception as e:
        logging.error(f"Error in Day_of_week_call: {e}")
        Day_of_week_call = ""
    
    try:
        now = datetime.datetime.now()
        Hour_of_crash_call = " AND (Hour_of_crash = {x2} OR Hour_of_crash IS NULL)".format(x2=now.hour)
        logging.debug(f"Hour_of_crash_call = {Hour_of_crash_call}, no Errors")
    except Exception as e:
        logging.error(f"Error in Hour_of_crash_call: {e}")
        Hour_of_crash_call = ""
        
    try:
        lighting_condition = get_lighting_condition_on_road(latitude,longitude,str(now.hour)+":00")
        lighting_condition_call = " AND (Lighting = \'{x1}\' OR Lighting IS NULL OR Lighting = \'unknown\')"

        if lighting_condition == "dawn_dusk":
            lighting_condition_call = lighting_condition_call.format(x1="dawn_dusk")
        elif lighting_condition == "daylight":
            lighting_condition_call = lighting_condition_call.format(x1="daylight")
        elif lighting_condition == "darkness_not_lit":
            lighting_condition_call = lighting_condition_call.format(x1="darkness_not_lit")
        else:
            lighting_condition_call = lighting_condition_call.format(x1="other")

        logging.debug(f"lighting_condition_call = {lighting_condition_call}, no Errors")
    except Exception as e:
        logging.error(f"Error in lighting_condition_call: {e}")
        lighting_condition_call = ""

    try:
        weather, road_weat = get_decoded_weather_on_road_rn(latitude,longitude)
        weather = weather.lower()

        road_weat_condition_call = " AND Road_wet = {x1}".format(x1 = int(road_weat))
        weather_condition_cal = " AND (Weather = \'{x1}\' OR Weather IS NULL OR Weather = \'unknown\')"

        if "rain" in weather:
            weather_condition_cal = weather_condition_cal.format(x1 = "rain")
        elif "snow" in weather:
            weather_condition_cal = weather_condition_cal.format(x1 = "snow")
        elif "fog" in weather:
            weather_condition_cal = weather_condition_cal.format(x1 = "fog OR Weather IS mist")
        elif "overcast" in weather:
            weather_condition_cal = weather_condition_cal.format(x1 = "overcast")
        elif ("clear sky" == weather) or ("mainly clear" == weather) or ("partly cloudy" == weather):
            weather_condition_cal = weather_condition_cal.format(x1 = "fine")
        else:
            weather_condition_cal = weather_condition_cal.format(x1 = "other")

        logging.debug(f"road_weat_condition_call = {road_weat_condition_call}, no Errors")
        logging.debug(f"weather_condition_cal = {weather_condition_cal}, no Errors")
    except Exception as e:
        logging.error(f"Error in weather_condition_cal or road_weat_condition_call: {e}")
        road_weat_condition_call = ""
        weather_condition_cal = ""

   
    additional_values_for_call = " AND Intersection = {intr_value} AND Midlock IS {mid_lock_value}"


    if (value is None) or (value == ""):
        logging.warning("value was None")
        return call_to_db(Day_of_week_call,Hour_of_crash_call,lighting_condition_call,road_weat_condition_call,weather_condition_cal)
    
    elif value == "straight road":
        logging.debug("processing straight road")
        '''additional_values_for_call = additional_values_for_call.format(intr_value = 0,  mid_lock_value = 0)
        logging.debug(f"additional_values_for_call = {additional_values_for_call}")'''
        ultimate_call_to_omnissiah += additional_values_for_call.format(intr_value = 0,  mid_lock_value = 0)
        logging.debug(f"additional_values_for_call = {additional_values_for_call}")
        return call_to_db(Day_of_week_call,Hour_of_crash_call,lighting_condition_call,road_weat_condition_call,weather_condition_cal,'')
    
    elif "turn" in value:
        logging.debug("processing turn")
        ultimate_call_to_omnissiah += additional_values_for_call.format(intr_value = 1,  mid_lock_value = 0)
        logging.debug(f"additional_values_for_call = {additional_values_for_call}")
        return call_to_db(Day_of_week_call,Hour_of_crash_call,lighting_condition_call,road_weat_condition_call,weather_condition_cal,additional_values_for_call)
    
    elif "mid-lock" == value:
        logging.debug("processing mid-lock")
        ultimate_call_to_omnissiah += additional_values_for_call.format(intr_value = 0,  mid_lock_value = 1)
        logging.debug(f"additional_values_for_call = {additional_values_for_call}")
        return call_to_db(Day_of_week_call,Hour_of_crash_call,lighting_condition_call,road_weat_condition_call,weather_condition_cal,additional_values_for_call)
    
    elif value in ["roundabout","u-turn"]:
        logging.debug("processing roundabout/u-turn")
        ultimate_call_to_omnissiah += additional_values_for_call.format(intr_value = 1,  mid_lock_value = 0)
        logging.debug(f"additional_values_for_call = {additional_values_for_call}")
        return call_to_db(Day_of_week_call,Hour_of_crash_call,lighting_condition_call,road_weat_condition_call,weather_condition_cal,additional_values_for_call)
    


    
latitude,longitude = 59.325,18.05
str_to_db_return_all_values(latitude,longitude)


