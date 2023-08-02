from prog import *

inp = get_input(sample = True)

expected_inp = [
        ["abc"],

        ["a", "b", "c"],

        ["ab", "ac"],

        ["a", "a", "a", "a"],

        ["b"]
        ]
expected_result_1 = 11
expected_result_2 = 6

print(inp == expected_inp)

print(get_result(inp) == expected_result_1)

print(get_result(inp, part = 2) == expected_result_2)
