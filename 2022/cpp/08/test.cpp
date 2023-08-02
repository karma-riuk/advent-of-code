#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1
TEST_CASE("Part 1") {
    Input actual_input = get_input("sample1");

    Input expected_input;
    expected_input.width = 5;
    for (auto t : {
             '3',
             '0',
             '3',
             '7',
             '3',
             '2',
             '5',
             '5',
             '1',
             '2',
             '6',
             '5',
             '3',
             '3',
             '2',
             '3',
             '3',
             '5',
             '4',
             '9',
             '3',
             '5',
             '3',
             '9',
             '0',
         }) {
        expected_input.trees.push_back(t);
    };
    SUBCASE("Testing input is parsed correctly") {
        CHECK(actual_input == expected_input);
    }

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "21");
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2") {
    Input actual_input = get_input("sample2");

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "8");
    }
}
#endif
