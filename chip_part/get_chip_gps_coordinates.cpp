#include <stdio.h>
#include <tuple>

std::tuple<double, double> chip_gps_coord_rn(double lan,double lon){
     /*
    Its a temp fix, because i didn't have a necessarily ships at the time of codin the project
    */
    return  std::make_tuple(lon,lan);
}

