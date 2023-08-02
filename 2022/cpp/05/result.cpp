#include "answer.hpp"
#include <iostream>


int main(int argc, char *argv[]) {
    if (argc < 2)
        error("Please specify the input file as first argument.");

#if !VERBOSE
    std::cout.setstate(std::ios_base::failbit);
#endif

    Input input = get_input(argv[1]);
    std::string result = get_result(input);

#if !VERBOSE
    std::cout.clear();
#endif

    std::cout << result << std::endl;

    return 0;
}
