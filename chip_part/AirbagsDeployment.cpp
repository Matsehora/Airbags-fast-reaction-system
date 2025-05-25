#include <iostream>
#include <chrono>//time to run the program
using namespace std;

void deploy(std::string value){
    cout << value << "was deployd"<< endl;
}

void deployAirbegs(long what_to_do){
    auto start = std::chrono::high_resolution_clock::now(); //time to run the program, start
    int temp = what_to_do, divisor = 1;
    while (temp >= 10) {
        temp /= 10;
        divisor *= 10;
    }

    // Extract digits one by one from left to right
    while (divisor > 0) {
        int digit = what_to_do / divisor; // Get the leftmost digit
        
        switch (digit) {
            case 1:
                deploy("Front Airbags");
                break;
            case 2:
                deploy("Side Airbags");
                break;
            case 3:
                deploy("Curtain Airbags");
                break;
            case 4:
                deploy("Knee Airbags ");
                break;
            case 5:
                deploy("Rear Airbags ");
                break;
            case 6:
                deploy("Seatbelt Airbags ");
                break;
            case 7:
                deploy("Center Airbags");
                break;
            case 8:
                deploy("Pedestrian Airbags");
                break;
            case 9:
                deploy("All");
                break;
        }


        what_to_do %= divisor; // Remove the leftmost digit
        divisor /= 10; // Move to the next digit
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start; //time to run the program, end
    std::cout << "Program ran for " << duration.count() << " seconds." << std::endl;
}

