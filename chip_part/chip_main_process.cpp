#include "cpp_shared_memory.cpp"
#include "get_chip_gps_coordinates.cpp"
#include "stres_code.cpp"
#include "check_if_car_get_hit.cpp"
#include "get_shock_sensors_values.cpp"
#include <tuple>
#include "car_rollover.cpp"
#include "OutputSimulatorForTheModules/MEMS.cpp"
#include "AirbagsDeployment.cpp"
#include "find_speed_of_the_car.cpp"
#include "OutputSimulatorForTheModules/MEMS.cpp"

void check_if_cases_mutch(int firstTwoDigitsFromMain[3],int value_of_the_case, int AllExceptFirstTwoDigits[3]){
    for (int i = 0; i < 3; i++ ){
        if( firstTwoDigitsFromMain[i] == value_of_the_case){
            deployAirbegs(AllExceptFirstTwoDigits[i])
            break;
        }
    }
}


int main(int argc, char const *argv[])
{

    while (true)
    {
        
        auto [SSV1,SSV2,SSV3,SSV4,SSV5,SSV6] =  chip_shock_sensors();
        auto [sv1, sv2, sv3] = receive_three_longs_from_python();
        std::cout << sv1;
        std::cout << sv2;
        std::cout << sv3;
        if detectRollover(readFloatGyroX(0),readFloatGyroY(0)){
            deployAirbegs(9); //all
        }
        else if( HasTheCarBeenHit(SSV1,SSV2,SSV3,SSV4,SSV5,SSV6)){
            if (150 < get_speed_of_the_car(40,readFloatAccelX(0))){
                deployAirbegs(9); //all
            }
            else{
                double max1 = numeric_limits<double>::lowest();
                double max2 = numeric_limits<double>::lowest();
                double values[] = {SSV1,SSV2,SSV3,SSV4,SSV5,SSV6};
                if (sv1 != NULL || sv2 != NULL || sv3 != NULL)
                {
                    // Find 2 max values
                    for (double v : values) {
                        if (v > max1) {
                            max2 = max1;
                            max1 = v;
                        } else if (v > max2) {
                            max2 = v;
                        }
                    }

                    int numbers[] = {sv1,sv2,sv3}; // Input numbers
                    int firstTwoDigits[3];
                    int AllExceptFirstTwoDigits[3];

                    // reducing values to 2 digits, and writing them in first Two Digits
                    for (int i = 0; i < 3; i++) {
                        int num = numbers[i];
                
                        // Find the number of digits in the number
                        int numDigits = 0;
                        int temp = num;
                        while (temp > 0) {
                            numDigits++;
                            temp /= 10;
                        }
                
                        // Extract the first two digits
                        int firstTwo = num / pow(10, numDigits - 2);
                
                        // Extract the remaining digits
                        int rest = num % static_cast<int>(pow(10, numDigits - 2));
                
                        firstTwoDigits[i] = firstTwo;
                        AllExceptFirstTwoDigits[i] = rest;
                    }
                
                    if ((max1 == SSV1 || max2 == SSV1) && (max1 == SSV2 || max2 == SSV2)) {
                        // frontal (11)
                        check_if_cases_mutch(firstTwoDigits,11,AllExceptFirstTwoDigits);
                    } else if ((max1 == SSV2 || max2 == SSV2) && (max1 == SSV3 || max2 == SSV3)) {
                        // frontal right (21)
                        check_if_cases_mutch(firstTwoDigits,21,AllExceptFirstTwoDigits);
                    } else if ((max1 == SSV3 || max2 == SSV3) && (max1 == SSV4 || max2 == SSV4)) {
                        // rear right (34)
                        check_if_cases_mutch(firstTwoDigits,34,AllExceptFirstTwoDigits);
                    } else if ((max1 == SSV4 || max2 == SSV4) && (max1 == SSV5 || max2 == SSV5)) {
                        // rear (44)
                        check_if_cases_mutch(firstTwoDigits,44,AllExceptFirstTwoDigits);
                    } else if ((max1 == SSV5 || max2 == SSV5) && (max1 == SSV6 || max2 == SSV6)) {
                        // rear left (43)
                        check_if_cases_mutch(firstTwoDigits,43,AllExceptFirstTwoDigits);
                    } else if ((max1 == SSV1 || max2 == SSV1) && (max1 == SSV6 || max2 == SSV6)) {
                        // frontal left (12)
                        check_if_cases_mutch(firstTwoDigits,12,AllExceptFirstTwoDigits);
                    }
                    else{
                        stress_mode(SSV1,SSV2,SSV3,SSV4,SSV5,SSV6,max1,max2);
                    }
                }
                else{
                    long what_to_do = stress_mode(SSV1,SSV2,SSV3,SSV4,SSV5,SSV6,max1,max2);
                    deployAirbegs(what_to_do);
                }
                
                auto [lon,lan] = chip_gps_coord_rn(53.0758,8.8078);
                send_floats_to_python(lan,lon);
            }
        }
        //_sleep(2000); //WARNING : USE ONLY FOR TEST CASES
    }
    
    return 0;
}

