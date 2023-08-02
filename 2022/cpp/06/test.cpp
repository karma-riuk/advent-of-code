#include <ostream>
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest/doctest/doctest.h"
#include "answer.hpp"

#if PART == 1

TEST_CASE("Part 1") {
    std::vector<Input> expected_inputs;
    expected_inputs.insert(expected_inputs.end(),
        {
            {"mjqjpqmgbljsphdztnvjfqwrcgsmlb"},
            {"bvwbjplbgvbhsrlpgdmjqwftvncz"},
            {"nppdvjthqldpwncqszvftbrmjlhg"},
            {"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"},
            {"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"},
        });

    std::vector<std::string> expected_outputs;
    expected_outputs.insert(expected_outputs.end(),
        {
            "7",
            "5",
            "6",
            "10",
            "11",
        });

    for (int i : {0, 1, 2, 3, 4}) {
        Input expected_input = expected_inputs[i];

        std::string sample_name = "sample" + std::to_string(i + 1);
        Input actual_input = get_input(sample_name.c_str());

        SUBCASE("Testing input is parsed correctly") {
            CHECK(actual_input == expected_input);
        }

        SUBCASE("Testing output is the one expected from AOC") {
            CHECK(get_result(actual_input) == expected_outputs[i]);
        }
    }
}
#endif

#if PART == 2
TEST_CASE("Part 2") {
    std::vector<std::string> expected_outputs;
    expected_outputs.insert(expected_outputs.end(),
        {
            "19",
            "23",
            "23",
            "29",
            "26",
        });

    for (int i : {0, 1, 2, 3, 4}) {
        std::string sample_name = "sample" + std::to_string(i + 1);
        Input actual_input = get_input(sample_name.c_str());

        SUBCASE("Testing output is the one expected from AOC") {
            CHECK(get_result(actual_input) == expected_outputs[i]);
        }
    }
}
#endif
