import logging

logger_static_annalysis_sub_function = logging.getLogger("Logger_static_annalysis_sub_function")
logger_static_annalysis_sub_function.setLevel(logging.DEBUG)
file_handler1 = logging.FileHandler("static_annalysis_sub_function.log")
formatter1 = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler1.setFormatter(formatter1)
logger_static_annalysis_sub_function.addHandler(file_handler1)

def sub_funcyion_for_one_severity(sorted_severity_dict:list,sorted_speed_limit_dict:list,sorted_traffic_controls_dict:list,sorted_crash_typ_dict:list,sorted_injuries:list):
        list_to_return_one_severity = []
        x = 0, y = 0, z = 0, i = 0
        for _ in range(8):
            list_to_return_one_severity.append([sorted_severity_dict[0],sorted_speed_limit_dict[x],sorted_traffic_controls_dict[y],sorted_crash_typ_dict[z],sorted_injuries[i],])
            x, y, z, i = (
            (x+1, y, z, i) if x==y==z==i else
            (x-1, y+1, z, i) if x>y else
            (x, y-1, z+1, i) if y>z else
            (x, y, z-1, i+1) if z>i else
            (i, i, i, i))

        logger_static_annalysis_sub_function.debug(f'List of the values from static analysis {list_to_return_one_severity}')    
        return list_to_return_one_severity

        

def sub_funcyion_for_more_than_one_severity(sorted_severity_dict:list,sorted_speed_limit_dict:list,sorted_traffic_controls_dict:list,sorted_crash_typ_dict:list,sorted_injuries:list):
    list_to_return_severity = []
    lenth_values =[[6,2],
                   [5,3,1],
                   [4,2,1,1],
                   [3,2,1,1,1],
                   [3,1,1,1,1,1]]
    
    value_to_take = sorted_severity_dict.count()-2
    logger_static_annalysis_sub_function.debug(f"List of values that expexted{lenth_values[value_to_take]}")
    itter_severity = 0
    for itter in lenth_values[value_to_take]:
        x = 0, y = 0, z = 0, i = 0
        for _ in range(itter):
            list_to_return_severity.append([sorted_severity_dict[itter_severity],sorted_speed_limit_dict[x],sorted_traffic_controls_dict[y],sorted_crash_typ_dict[z],sorted_injuries[i],])
            x, y, z, i = (
            (x+1, y, z, i) if x==y==z==i else
            (x-1, y+1, z, i) if x>y else
            (x, y-1, z+1, i) if y>z else
            (x, y, z-1, i+1) if z>i else
            (i, i, i, i))
        itter_severity += 1

    logger_static_annalysis_sub_function.debug(f'List of the values from static analysis {list_to_return_severity}')
    return list_to_return_severity


def analyze_values(sorted_Severity_dict:list,sorted_Speed_limit_dict:list,sorted_Traffic_controls_dict:list,sorted_Crash_typ_dict:list,sorted_injuries:list):
    try:
        if min([len(sorted_Severity_dict),len(sorted_Speed_limit_dict),len(sorted_Traffic_controls_dict),len(sorted_Crash_typ_dict),len(sorted_injuries)]) != 0:
            if sorted_Severity_dict.count() == 1:
                logger_static_annalysis_sub_function.debug("sorted_Severity_dict was 1, proceed to the sub_funcyion_for_one_severity")
                return sub_funcyion_for_one_severity(sorted_Severity_dict,sorted_Speed_limit_dict,sorted_Traffic_controls_dict,sorted_Crash_typ_dict,sorted_injuries)
            else:
                logger_static_annalysis_sub_function.debug("sorted_Severity_dict was more then 1, proceed to the sub_funcyion_for_one_severity")
                return sub_funcyion_for_more_than_one_severity(sorted_Severity_dict,sorted_Speed_limit_dict,sorted_Traffic_controls_dict,sorted_Crash_typ_dict,sorted_injuries)
        else:
            return None
    except Exception as e:
        logger_static_annalysis_sub_function.error(e)
        return None





