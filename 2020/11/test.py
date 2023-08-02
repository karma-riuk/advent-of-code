from prog import *

inp = get_input(sample = True)

result_1 = get_result(inp)
expected_1 = 37

print(f"{result_1 = } {result_1 == expected_1}")
print()

inp_no_occupied = get_input(sample = True, sample_name = "sample_no_occupied")
print(count_occupied_direction(3, 3, inp_no_occupied))

result_2 = get_result(inp, part = 2)
expected_2 = 26
print(f"{result_2 = } {result_2 == expected_2}")
