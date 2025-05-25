#include "OutputSimulatorForTheModules/GPS.cpp"
#include <cmath>  // For fabs()

const float ACCEL_THRESHOLD = 0.1;  // Ignore small accelerations (in g)
const float TIME_STEP = 0.01;       // Time step in seconds (10ms loop)
const float G_TO_MS2 = 9.81;        // Convert g to m/s²
  

// Function to calculate speed in km/h
float getSpeedUsingAcceleration(float accelX) {
    float velocity = 0.0; // Speed in m/s
    float acceleration_m_s2 = accelX * G_TO_MS2;  // Convert g to m/s²

    // Ignore small accelerations to reduce drift
    if (fabs(acceleration_m_s2) < ACCEL_THRESHOLD) {
        acceleration_m_s2 = 0;
    }

    // Integrate acceleration to get velocity
    velocity += acceleration_m_s2 * TIME_STEP;

    // Convert m/s to km/h
    return velocity * 3.6;
}

/*
Metod above, is using built in accelerometer, in MEMS chip, so it can calculate the speed of the car
its not very accurate so it's back up for a GPS metod
*/


float get_speed_of_the_car(float speed_for_the_gps_moduel,float accelX){
    if SpeedSsValid(kmh(speed_for_the_gps_moduel)){
        return kmh(speed_for_the_gps_moduel)
    }
    else{
        return getSpeedUsingAcceleration(accelX)
    }

}