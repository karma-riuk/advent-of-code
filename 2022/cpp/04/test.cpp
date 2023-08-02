#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1
TEST_CASE("Part 1"){ 
    std::vector<Input> expected_input; 
    expected_input.insert(expected_input.end(), {
            {{2, 4}, {6, 8}},
            {{2, 3}, {4, 5}},
            {{5, 7}, {7, 9}},
            {{2, 8}, {3, 7}},
            {{6, 6}, {4, 6}},
            {{2, 6}, {4, 8}},
            });
    std::vector<Input> actual_input = get_input("sample1"); 

    SUBCASE("Testing input is parsed correctly"){
        CHECK(actual_input == expected_input);
    }

    SUBCASE("Testing output is the one expected from AOC"){
        CHECK(get_result(actual_input) == "2");
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2"){ 
    std::vector<Input> actual_input = get_input("sample1"); 
    SUBCASE("Testing output is the one expected from AOC"){
        CHECK(get_result(actual_input) == "4");
    }
}
#endif
