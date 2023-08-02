// AOC - 2022 - DATE
#include "answer.hpp"

#include <fstream>
#include <iostream>

Input get_input(const char* filename) {
    std::ifstream stream(filename);
    std::string str;
    Input ret;

    while (getline(stream, str)) {}
    return ret;
}

std::string get_result(Input& input) {
    std::string ret;
#if PART == 1
#else
#endif
    return ret;
}
