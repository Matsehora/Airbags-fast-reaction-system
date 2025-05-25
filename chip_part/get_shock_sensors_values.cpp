#include <stdio.h>
#include <tuple>

std::tuple<double, double,double, double,double, double> chip_shock_sensors(double v1 = 0,double v2= 0,double v3= 0,double v4= 0,double v5= 0,double v6= 0){
    /*
    Its a temp fix, because i didn't have a necessarily ships at the time of codin the project

    v1 - front left conor
    v2 - front right conor
    v3 - right side of the car
    v4 - beck left conor
    v5 - beck right conor
    v6 - left side of the car

    */
    return  std::make_tuple(v1,v2,v3,v4,v5,v6);
}

