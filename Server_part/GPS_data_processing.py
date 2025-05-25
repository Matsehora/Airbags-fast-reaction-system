from static_analysis import static_analysis_from_db
from path_to_list import get_route_details_with_coords
from dotenv import load_dotenv
import os
from shared_memory import send_three_longs_to_cpp, receive_floats_from_cpp
from proximity_check import is_within_2m
from what_to_do_based_on_static_analysis import what_to_do_ret_long
import logging



def reset_program():
    first_run = True
    route_events, event_coords = None
    pointer = 0

load_dotenv("API_keys.env")
api_key = os.getenv("openrouteservice_api_key")

logger1 = logging.getLogger("Logger1")
logger1.setLevel(logging.DEBUG)
file_handler1 = logging.FileHandler("GPS_DATA_help.log")
formatter1 = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler1.setFormatter(formatter1)
logger1.addHandler(file_handler1)



#route_events, event_coords = None
first_run = True
pointer = 0
error_counter = 0
while True:
    try:
        #if (route_events is None) and (event_coords is None):
        if (first_run):  
            #start_point = (8.8078, 53.0758)  # Bremen city center
            #end_point = (9.72970425846439,52.37549667131688)
            start_point = (13.504305,43.603181)
            end_point = (12.919927,43.901394)
            route_events, event_coords = get_route_details_with_coords(start_point , end_point, api_key)
            first_run = False
            logger1.debug(first_run)
    except Exception as e:
        logger1.error(f"{e}, Error acupaid while trying to process rout")
        #print(f"{e},error")
        send_three_longs_to_cpp(8,8,8)
        error_counter += 1
        pointer += 1

    try:
        
        if pointer == 0:
            
            st_from_db = static_analysis_from_db(event_coords[pointer][1],event_coords[pointer][0],route_events[pointer])
            logger1.debug(st_from_db,"st_from_db", len(st_from_db))
            if st_from_db is not None:
                logger1.debug("data are in if")
                long_list = what_to_do_ret_long(st_from_db)
                logger1.debug(long_list,long_list)
                send_three_longs_to_cpp(long_list[0],long_list[1],long_list[2],long_list[3],long_list[4],long_list[5],long_list[6],long_list[7])
            else:
                logger1.error(f"data was null")
                send_three_longs_to_cpp(8,8,8)
            pointer += 1
            #print(pointer,"pointer")
    except Exception as e:
        logger1.error(f"{e}, Error acupaid while trying to process path")
        #print(e)
        send_three_longs_to_cpp(8,8,8)
        error_counter += 1



    try:
        car_position_rn = receive_floats_from_cpp()
        #print(car_position_rn)
        if (is_within_2m(event_coords[pointer],car_position_rn)):
            st_from_db = static_analysis_from_db(event_coords[pointer][1],event_coords[pointer][0],route_events[pointer])
            long_list = what_to_do_ret_long(static_analysis_from_db)
            send_three_longs_to_cpp(long_list[0],long_list[1],long_list[2])
            pointer += 1
    except Exception as e:
        logger1.error(f"{e}, Error acupaid while trying to process car cordinats")
        send_three_longs_to_cpp(8,8,8)
        #print(e)
        error_counter += 1
    if (pointer == (len(event_coords)-1)) or (error_counter == (len(event_coords)/2)):
        reset_program()


