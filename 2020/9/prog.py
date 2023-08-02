import yaml

def get_input(sample = False):
    with open('sample' if sample else 'input', 'r') as f:
        return [int(line) for line in f.readlines()]


def get_preamble(data: list, size: int):
    preamble = {}

    for i in range(size):
        x = data[i]
        for j in range(i + 1, size):
            y = data[j]
            preamble[(x, y)] = x + y

    return preamble

def print_preamble(dic: dict):
    for keys, value in dic.items():
        print(f"{keys}: {value}")

def get_result(data: list, part = 1, sample = False):
    if part == 1:
        pre_size = 5 if sample else 25
        preamble = get_preamble(data, pre_size)

        for i in range(pre_size, len(data)):

            elem = data[i]

            if elem not in preamble.values():
                return elem

            elem_to_pop = data[i - pre_size]
            new_preamble = {}
            for keys, value in preamble.items():
                if elem_to_pop not in keys:
                    new_preamble[keys] = value
            preamble = new_preamble

            for p in range(i - pre_size + 1, i):
                elem_p = data[p]
                preamble[(elem, elem_p)] = elem_p + elem

    else:
        objective = get_result(data, part = 1, sample = sample)
        for length in range(2, len(data)):
            for i in range(len(data) - length):
                tmp = data[i:i+length]
                if sum(tmp) == objective:
                    return min(tmp) + max(tmp)



if __name__ == "__main__":
    print(get_result(get_input(), part = 2))

