VERBOSE = True
def verbose(s = "", **kwargs):
    if VERBOSE:
        print(s, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return list(map(lambda x: int(x), f.readlines()[0].split(',')))


def result(inp, part = 1):
    res = -1

    for mid in range(min(inp), max(inp) + 1):
        score = 0
        for n in inp:
            delta = abs(mid - n)
            if part == 1:
                score += delta
            else:
                score += delta * (delta + 1) / 2
        res = score if score < res or res == -1 else res

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
