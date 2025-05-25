def what_to_do_ret_long(list_of_data):
    """   
    returns list of 3 set of long -> 0 1 2 3 4 5 6 7 8 9

    first 0 1 always reserved for the calishion type

    21 - left side 
    12 - right side 
    11 - front 
    44 - rear
    99 - unknown cose
    21 - frontal right
    34 - rear right
    43 - rear left

    all other are for Airbags operating sequence

    0 - Not open
    1 - Front Airbags 
    2 - Side Airbags 
    3 - Curtain Airbags 
    4- Knee Airbags 
    5 - Rear Airbags 
    6- Seatbelt Airbags  
    7 -Center Airbags  
    8 - Pedestrian Airbags
    9 - open all at the same time

    example 
    449 - rear end collision open all airbags 
    111456 - front end coloshion, opne airbegs in sequence Front Airbags -> Knee Airbags -> Rear Airbags -> Seatbelt Airbags
    0 - property damage
    
    """
   
    list_for_return_thre_long = []
    for x in list_of_data:
        list_for_return_thre_long.append(evaluate_what_to_do(x))

    return list_for_return_thre_long


def check_for_injuris(str_value:str):
    if str_value == "property_damage":
        return 0
    elif str_value == "fatality":
        return 999
    else: return None

    

def evaluate_what_to_do(slise_of_data:list):
    right_angle_collision = ["Right Angle", "Right Angle Involving Parking", "Right Angle Entering / Leaving Driveway", "Right Angle Involving Overtaking", "Right Angle Involving Pedestrian"]
    rear_end_collision = ["Rear End", "Rear End Involving Parking", "Rear End Involving Overtaking", "Rear End Entering / Leaving Driveway", "Rear End Involving Pedestrian", "Rear End Involving Animal"]
    side_swipe_collision = ["Side Swipe", "Sideswipe Same Dirn Involving Overtaking", "Sideswipe Same Dirn Involving Parking", "Sideswipe Same Dirn Entering / Leaving Driveway", "Sideswipe Same Dirn Involving Animal", "Sideswipe Same Dirn Involving Pedestrian"]
    head_on_collision = ["Head On", "Head On Involving Overtaking", "Head On Entering / Leaving Driveway", "Head On Involving Animal", "Head On Involving Parking", "Head On Involving Pedestrian"]
    right_turn_collision = ["Right Turn", "Right Turn Thru Entering / Leaving Driveway", "Right Turn Thru Involving Pedestrian", "Right Turn Thru Involving Parking", "Right Turn Thru Involving Overtaking"]
    left_road_out_of_control = ["Left Road - Out of Control"]
    hit_pedestrian = ["Hit Pedestrian", "Hit Pedestrian Involving Pedestrian", "Hit Pedestrian Involving Parking", "Hit Pedestrian Involving Overtaking", "Hit Pedestrian Involving Animal"]
    hit_fixed_object = ["Hit Fixed Object", "Hit Object Involving Parking", "Hit Object Involving Pedestrian", "Hit Object Entering / Leaving Driveway", "Hit Object Involving Animal"]
    hit_object= ["Hit Object on Road"]
    hit_parked_object = ["Hit Parked Vehicle"]
    hit_animal = ["Hit Animal", "Struck Animal", "Hit Animal Involving Animal", "Hit Animal Involving Parking"]
    rollover_collision = ["Roll Over", "Vehicle overturned (no collision)"]
    collision_with = ["Collision with vehicle","Collision with a fixed object","collision with some other object"]



    data_3 = slise_of_data[8]
    if data_3 in [None, "Other", "Other accident"]:
        return None
    
    if data_3 in right_angle_collision:
        return 21123  # Frontal Right Collision -> Front Airbags -> Side Airbags -> Curtain Airbags
    elif data_3 in rear_end_collision:
        return 446137  # Rear Collision -> Seatbelt Airbags -> Rear Airbags -> Curtain Airbags -> Center Airbags
    elif data_3 in side_swipe_collision:
        return 2123  # Right Side Collision -> Side Airbags -> Curtain Airbags
    elif data_3 in head_on_collision:
        return 111456  # Front Collision -> Front Airbags -> Knee Airbags -> Rear Airbags -> Seatbelt Airbags
    elif data_3 in right_turn_collision:
        return 2112  # Frontal Right -> Front Airbags -> Side Airbags
    elif data_3 in left_road_out_of_control:
        return 211236  # Frontal Right Collision -> Front -> Side -> Curtain -> Seatbelt Airbags
    elif data_3 in hit_pedestrian:
        return 1118  # Front Collision -> Front Airbags -> Pedestrian Airbags
    elif data_3 in hit_fixed_object:
        return 1114  # Front Collision -> Front Airbags -> Knee Airbags
    elif data_3 in hit_object:
        return 1114  # Front Collision -> Front Airbags -> Knee Airbags
    elif data_3 in hit_parked_object:
        return 446137  # Rear Collision -> Seatbelt Airbags -> Rear Airbags -> Curtain Airbags -> Center Airbags
    elif data_3 in hit_animal:
        return 1114  # Front Collision -> Front Airbags -> Knee Airbags
    elif data_3 in rollover_collision:
        return 337  # Rollover -> Curtain Airbags -> Center Airbags
    elif data_3 in collision_with:
        return 1114  # Generic Collision -> Front Airbags -> Knee Airbags
    else:
        return 999  # Unknown Case

