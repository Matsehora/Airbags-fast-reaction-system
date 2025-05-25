from str_value_to_data_from_db import str_to_db_return_all_values
import logging
from static_annalysis_sub_function import analyze_values
#1590854

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename="static_analysis.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def static_analysis_from_db(latitude,longitude,str_for_db_call:str):
    """
    Use latitude and longitude for get data from get_lighting_condition and get_the_weather 

    str call is "straight road"
                "turn left"
                "turn right"
                "roundabout"
                "u-turn"
    from path_to_list.py, value can also be None
    
    """
    

    logging.debug("start of the static_analysis_from_db")
    try:
        raw_data_from_db = str_to_db_return_all_values(latitude,longitude,str_for_db_call)
        logging.debug("Data was extracted successfully")
    except Exception as e:
        logging.error(f"Error happened while trying to pull data from db: {e}")
        logging.warning("Sending back None, program will run some time in emergency state")
        return None
    
    if (raw_data_from_db is not None) and (0<len(raw_data_from_db)):
        # extracting data from raw data from_db 
        #and writing in data only Severity, Speed_limit,Crash_type,Traffic_controls, Fatalities,Serious_injuries,Minor_injuries
        data = [[ds[3], ds[4], ds[12], ds[14], ds[15], ds[16],ds[17]] for ds in raw_data_from_db]
        logging.debug("Data was extracted successfully from raw_data")

        Severity_dict = dict()
        Speed_limit_dict = dict()
        Traffic_controls_dict = dict()
        Crash_typ_dict = dict()
        injuries = dict()
        
        logging.debug(len(data))

        for x in data:
            try:
                Severity_dict[x[0]] = Severity_dict.get(x[0], 1) + 1
                Speed_limit_dict[x[1]] = Speed_limit_dict.get(x[1], 1) + 1
                Crash_typ_dict[x[2]] = Traffic_controls_dict.get(x[2], 1) + 1
                Traffic_controls_dict[x[3]] = Traffic_controls_dict.get(x[3], 1) + 1
            
                if all(x[i] is not None for i in [4, 6]):
                    inj_sum = ((x[4]*3) + (x[5]*2) + x[6] )
                    injuries[inj_sum]  = injuries.get(x[inj_sum], 1) + 1
                else:
                    injuries[None]  = injuries.get(None, 1) + 1
            except Exception as e:
                logging.error(f"{e}, in for while procesing data")
                logging.error(x)
                break

        logging.debug(Severity_dict)
        logging.debug(Speed_limit_dict)
        logging.debug(Crash_typ_dict)
        logging.debug(Traffic_controls_dict)
        logging.debug(injuries)

    
        try:
            for x in [None,'none','None']:
                Severity_dict.pop(x,False)
                Speed_limit_dict.pop(x,False)
                Traffic_controls_dict.pop(x,False)
                Crash_typ_dict.pop(x,False)
                injuries.pop(x,False)
            logging.debug("Pop of None values was successful")
            
            sorted_Severity_dict = dict(sorted(Severity_dict.items(), key=lambda item: item[1], reverse=True))
            sorted_Speed_limit_dict = dict(sorted(Speed_limit_dict.items(), key=lambda item: item[1], reverse=True))
            sorted_Traffic_controls_dict = dict(sorted(Traffic_controls_dict.items(), key=lambda item: item[1], reverse=True))
            sorted_Crash_typ_dict = dict(sorted(Crash_typ_dict.items(), key=lambda item: item[1], reverse=True))
            sorted_injuries = dict(sorted(injuries.items(), key=lambda item: item[1], reverse=True))
            logging.debug("Sort of dict was successful")

            logging.debug(sorted_Severity_dict)
            logging.debug(sorted_Speed_limit_dict)
            logging.debug(sorted_Traffic_controls_dict)
            logging.debug(sorted_Crash_typ_dict)
            logging.debug(sorted_injuries)

            #decide what to send to the chip
            list_to_return = analyze_values(list(sorted_Severity_dict),list(sorted_Speed_limit_dict),list(sorted_Traffic_controls_dict,list(sorted_Crash_typ_dict),list(sorted_injuries)))

            logging.debug("List was successfuly formd")
            logging.debug(list_to_return)

            return list_to_return

        except KeyError as ke:
            logging.error(f"Error happened while trying to pop None from dict: {ke}")
            logging.warning("Sending back None, program will run some time in emergency state")
            return None
        except Exception as e:
            logging.error(f"Error happened while sorting data in dict: {e}")
            logging.warning("Sending back None, program will run some time in emergency state")
            return None

    else:
        logging.error("Data was None")
        logging.warning("Sending back None, program will run some time in emergency state")
        return None

'''latitude,longitude = 59.325,18.050
static_analysis_from_db(latitude,longitude,None)'''



