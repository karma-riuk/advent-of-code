VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return list(map(lambda x: int(x), f.readlines()[0].split(',')))


def create_state(l):
    return [0 for _ in range(l)]

def result(inp, days = 80):
    state = create_state(9)
    for n in inp:
        state[n] += 1

    for _ in range(days):
        zeros = state[0]
        for i, n in enumerate( state[1:] ):
            state[i] = n
        state[6] += zeros
        state[8] = zeros

    res = 0
    for n in state:
        res += n

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), days = 256))
