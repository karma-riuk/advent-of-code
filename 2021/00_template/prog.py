VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def result(inp, part = 1):
    res = 0;

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 1))
