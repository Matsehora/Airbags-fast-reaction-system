#include <iostream>
#include <fstream>
#include <tuple>
#include <vector>
#include <cstring>

// Function to receive three longs from Python
std::tuple<long long, long long, long long> receive_three_longs_from_python() {
    std::ifstream file("../Temp_shared_memory/3_long.txt", std::ios::binary);
    if (!file) {
        std::cerr << "Error: Failed to open 3_long.txt!" << std::endl;
        return {8, 8, 8};
    }
    
    long long received_longs[3] = {0};  // Ensure long long (8 bytes)
    file.read(reinterpret_cast<char*>(received_longs), sizeof(received_longs));
    file.close();
    
    return {received_longs[0], received_longs[1], received_longs[2]};
}


// Function to send (float, float) data to Python
void send_floats_to_python(float f1, float f2) {
    std::ofstream file("../Temp_shared_memory/2_float.txt", std::ios::binary | std::ios::trunc);
    if (!file) {
        std::cerr << "Error: Failed to open 2_float.txt!" << std::endl;
        return;
    }
    
    file.write(reinterpret_cast<char*>(&f1), sizeof(float));
    file.write(reinterpret_cast<char*>(&f2), sizeof(float));
    file.close();
}

/*int main() {
    while (true) {
        auto [long1, long2, long3] = receive_three_longs_from_python();
        std::cout << "C++ Received Longs: " << long1 << ", " << long2 << ", " << long3 << std::endl;

        float f1 = 3.14, f2 = 2.71;
        send_floats_to_python(f1, f2);
        std::cout << "C++ Sent Floats: " << f1 << ", " << f2 << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(1));  // Simulate processing delay
    }

    return 0;
}*/