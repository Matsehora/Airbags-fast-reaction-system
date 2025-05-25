/*
File to simulate output for GPS MODULE NEO-6M
Becose the libs grant the possibility to just get speed using speed.kmph() , this file will create a function for simulating this part of the moduel
*/

#include <cmath>

float kmh(float speed){
    return speed
}

bool SpeedSsValid(float value){
    if (std::isnan(value)) {
        return false
    } else {
        return true
    }
}