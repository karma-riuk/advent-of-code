def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        tmp =  [line.strip().split(' ') for line in f.readlines()]
        return [[e[0], int(e[1])] for e in tmp]


def result(inp, part = 1):
    hor = dep = 0
    if part == 1:
        for [cmd, n] in inp:
            if cmd == "forward":
                hor += n
            elif cmd == "down":
                dep += n
            elif cmd == "up":
                dep -= n
    else:
        aim = 0
        for [cmd, n] in inp:
            if cmd == "forward":
                hor += n
                dep += n * aim
            elif cmd == "down":
                aim += n
            elif cmd == "up":
                aim -= n
            # print(f"{cmd} {n}")
            # print(f"\t{aim = }, {hor = }, {dep = }")
    return hor * dep

if __name__ == "__main__":
    print(result(get_input(), part = 2))
