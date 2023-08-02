#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1
TEST_CASE("Part 1") {
    Input actual_input = get_input("sample1");

    Input expected_input;
    SUBCASE("Testing input is parsed correctly") {
        CHECK(actual_input == expected_input);
    }

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "SAMPLE1_OUT");
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2") {
    Input actual_input = get_input("sample2");

    Input expected_input;
    SUBCASE("Testing input is parsed correctly") {
        CHECK(actual_input == expected_input);
    }

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "SAMPLE2_OUT");
    }
}
#endif
