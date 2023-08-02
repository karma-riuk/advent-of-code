#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "answer.hpp"
#include "../doctest/doctest/doctest.h"

#ifdef SAMPLE1

TEST_CASE("Part 1"){ 
    std::vector<Input> expected_input; 

    Input elf1;
    elf1.calories.insert(elf1.calories.end(), {
            1000,
            2000,
            3000,
            });
    
    Input elf2;
    elf2.calories.insert(elf2.calories.end(), {
            4000,
            });

    Input elf3;
    elf3.calories.insert(elf3.calories.end(), {
            5000,
            6000,
            });

    Input elf4;
    elf4.calories.insert(elf4.calories.end(), {
            7000,
            8000,
            9000,
            });

    Input elf5;
    elf5.calories.insert(elf5.calories.end(), {
            10000
            });

    expected_input.insert(expected_input.end(), {
            elf1, elf2, elf3, elf4, elf5
            });


    std::vector<Input> actual_input = get_input("sample1"); 

    SUBCASE("Testing input is parsed correctly"){
        CHECK(actual_input == expected_input);
    }

    SUBCASE("Testing output is the one expected from AOC"){
        CHECK(get_result(actual_input) == "24000");
    }
}
#endif

#ifdef SAMPLE2
TEST_CASE("Part 2"){ 
    std::vector<Input> actual_input = get_input("sample2"); 

    SUBCASE("Testing output is the one expected from AOC"){
        CHECK(get_result(actual_input) == "45000");
    }
}
#endif
