#include <iostream>
#include "cpp_shared_memory.cpp"

int main() {

    int firstTwoDigits[3];
    int AllExceptFirstTwoDigits[3];

    for (int i = 0; i < 3; i++) {
        int num = numbers[i];
        std::string temp_value = std::to_string(num)
        firstTwoDigits[i] = std::to_integer(num[:2]);
        AllExceptFirstTwoDigits[i] = std::to_integer(num[2:]);
    }
}