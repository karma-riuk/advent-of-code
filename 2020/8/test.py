from prog import *

inp = get_input(sample = True)

result_1 = get_result(inp)
expected_1 = 5

print(f"{result_1 = } {result_1 == expected_1}")

result_2 = get_result(inp, part = 2)

expected_2 = 8
print(f"{result_2 = } {result_2 == expected_2}")
