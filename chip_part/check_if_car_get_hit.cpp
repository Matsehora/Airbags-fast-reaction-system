
#include <stdio.h>
#include <iostream>
#include <tuple>

bool HasTheCarBeenHit(double v1,double v2,double v3,double v4,double v5,double v6){
    

    bool allLessThan2000 = (v1 < 2000 && v2 < 2000 && v3 < 2000 && 
                             v4 < 2000 && v5 < 2000 && v6 < 2000);

    // Check if all values are zero
    bool allZero = (v1 == 0 && v2 == 0 && v3 == 0 && 
                    v4 == 0 && v5 == 0 && v6 == 0);

    std::cout << "All values < 2000? " << (allLessThan2000 ? "Yes" : "No") << std::endl;
    std::cout << "All values are 0? " << (allZero ? "Yes" : "No") << std::endl;

    bool end_of_call = allLessThan2000 || allZero;

    return end_of_call;

}