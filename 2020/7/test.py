from prog import *
import yaml

inp_1 = parse_input(get_input(sample = True))
inp_2 = parse_input(get_input(sample = True, sample_number = 2))


result_1 = get_result(inp_1)
print(f"{result_1 = }")
print(f"{result_1 == 4}")
print()


#  print(yaml.dump(inp_1))
result_2_1 = get_result(inp_1, part = 2)

print(f"{result_2_1 = }")
print(f"{result_2_1 == 32}")
print()

#  print(yaml.dump(inp_2))
result_2_2 = get_result(inp_2, part = 2)
print(f"{result_2_2 = }")
print(f"{result_2_2 == 126}")
print()

