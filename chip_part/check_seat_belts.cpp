#include <stdio.h>
#include <tuple>

std::tuple<bool, bool,bool, bool> seat_belts_buckled(bool driver = false,bool front_passenger = false, bool left_passenger = false, bool mild_and_right_passenger = false){
    /*
    Its a temp fix, because i didn't have a necessarily ships at the time of codin the project
    */
    return  std::make_tuple(driver,front_passenger,left_passenger,mild_and_right_passenger);
}
