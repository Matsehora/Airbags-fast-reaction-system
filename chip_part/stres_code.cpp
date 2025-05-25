#include <stdio.h>
#include <iostream>
#include <tuple>
#include <cstdlib>  // For strtol
#include <algorithm>
#include <limits> // Include limits for std::numeric_limits
#include "check_seat_belts.cpp"

using namespace std;

long stress_mode(double v1, double v2, double v3, double v4, double v5, double v6,double max1,double max2) {
    //string what_to_do_STR; // Example valid number as a string

    
    /*double max1 = numeric_limits<double>::lowest();
    double max2 = numeric_limits<double>::lowest();
    
    double values[] = {v1, v2, v3, v4, v5, v6};

    for (double v : values) {
        if (v > max1) {
            max2 = max1;
            max1 = v;
        } else if (v > max2) {
            max2 = v;
        }
    }
    */
    long what_to_do;

    std::cout << "Max1: " << max1 << ", Max2: " << max2 << "\n";
    // 5000 its a constant for a most car to strar cosing a harm to a human if nit activate airbegs
    
    if (5000<(max1+max2))
    {    
        
        auto [driver, front_passenger, left_passenger, mid_and_right_passenger] = seat_belts_buckled();
        if ((max1 == v1 || max2 == v1) && (max1 == v2 || max2 == v2)) {
            // frontal (11)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 111456;  // Front + Knee + Rear + Seatbelt Airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 11145;  // Front + Knee + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 1156;  // Rear + Seatbelt Airbags
            } else {
                what_to_do = 110;  // No airbags deploy
            }
        } else if ((max1 == v2 || max2 == v2) && (max1 == v3 || max2 == v3)) {
            // frontal right (21)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 211456;  // Front + Knee + Rear + Seatbelt Airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 21145;  // Front + Knee + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 2156;  // Rear + Seatbelt Airbags
            } else {
                what_to_do = 210;  // No airbags deploy
            }
        } else if ((max1 == v3 || max2 == v3) && (max1 == v4 || max2 == v4)) {
            // rear right (34)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 34156;  // Rear + Side + Curtain + Seatbelt Airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 3415;  // Rear + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 3456;  // Rear + Seatbelt Airbags
            } else {
                what_to_do = 340;  // No airbags deploy
            }
        } else if ((max1 == v4 || max2 == v4) && (max1 == v5 || max2 == v5)) {
            // rear (44)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 449;  // Open all airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 4456;  // Rear + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 446;  // Rear Airbags
            } else {
                what_to_do = 440;  // No airbags deploy
            }
        } else if ((max1 == v5 || max2 == v5) && (max1 == v6 || max2 == v6)) {
            // rear left (43)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 43156;  // Rear + Side + Curtain + Seatbelt Airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 4315;  // Rear + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 4356;  // Rear + Seatbelt Airbags
            } else {
                what_to_do = 430;  // No airbags deploy
            }
        } else if ((max1 == v1 || max2 == v1) && (max1 == v6 || max2 == v6)) {
            // frontal left (12)
            if ((driver || front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 121456;  // Front + Knee + Rear + Seatbelt Airbags
            } else if ((driver || front_passenger) && (!left_passenger && !mid_and_right_passenger)) {
                what_to_do = 12145;  // Front + Knee + Seatbelt Airbags
            } else if ((!driver && !front_passenger) && (left_passenger || mid_and_right_passenger)) {
                what_to_do = 1256;  // Rear + Seatbelt Airbags
            } else {
                what_to_do = 120;  // No airbags deploy
            }
        } else {
            what_to_do = 999;  // Unknown case
        }        
    }
    else what_to_do = 0;

    

    
    /*
    char* endptr;  // To check for conversion errors
    long what_to_do = strtol(what_to_do_STR.c_str(), &endptr, 10);

    // Check if the conversion was successful
    if (*endptr != '\0') {
        cerr << "Conversion failed! Invalid characters found: " << endptr << endl;
        return 9999999999; // Handle the error appropriately
    }
    */
    return what_to_do;
}