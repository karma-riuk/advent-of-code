#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1
TEST_CASE("Part 1") {
    std::vector<Input> expected_input;
    expected_input.insert(expected_input.end(), {
                                                    {.content = "vJrwpWtwJgWrhcsFMMfFFhFp"},
                                                    {.content = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"},
                                                    {.content = "PmmdzqPrVvPwwTWBwg"},
                                                    {.content = "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"},
                                                    {.content = "ttgJtRGJQctTZtZT"},
                                                    {.content = "CrZsJsPPZsGzwwsLwLmpwMDw"},
                                                });
    std::vector<Input> actual_input = get_input("sample1");

    SUBCASE("Testing input is parsed correctly") { CHECK(actual_input == expected_input); }

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "157");
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2") {
    std::vector<Input> actual_input = get_input("sample2");

    SUBCASE("Testing output is the one expected from AOC") {
        CHECK(get_result(actual_input) == "70");
    }
}
#endif
