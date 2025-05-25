// Define rollover thresholds (realistic values)
const float ROLL_THRESHOLD = 60.0;  // Roll rate in degrees per second (depends on vehicle type)
const float PITCH_THRESHOLD = 40.0; // Pitch rate in degrees per second

bool detectRollover(float gyroX, float gyroY) {
    // Check if roll or pitch rate exceeds the threshold
    if (fabs(gyroX) > ROLL_THRESHOLD || fabs(gyroY) > PITCH_THRESHOLD) {
        return true;  // Rollover is imminent
    }
    return false;
}

