def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def result(inp, part = 1):
    res = 0;
    if part == 1:
        prev = inp[0]
        for cur in inp[1:]:
            if prev <= cur:
                res += 1;
            prev = cur;
    else:
        prev = 0
        for cur in range(1, len(inp) - 2):
            if sum(inp[prev:prev+3]) < sum(inp[cur:cur+3]):
                res += 1;
            prev = cur;

    return res


if __name__ == "__main__":
    print(result(get_input(), part = 2))
