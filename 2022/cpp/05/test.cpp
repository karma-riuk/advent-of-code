#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1
TEST_CASE("Part 1") {
    Input expected_input{.stacks =
                             {
                                 {'Z', 'N'},
                                 {'M', 'C', 'D'},
                                 {'P'},
                             },
                         .moves = {
                             {0, 1, 0},
                             {2, 0, 2},
                             {1, 1, 0},
                             {0, 0, 1},
                         }};

    Input actual_input = get_input("sample1");
    std::cout << expected_input << std::endl;
    std::cout << actual_input << std::endl;

    SUBCASE("Testing input is parsed correctly") { CHECK(actual_input == expected_input); }

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "CMZ");
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2") {
    Input actual_input = get_input("sample2");

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "MCD");
    }
}
#endif
