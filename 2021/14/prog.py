VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        tmp = f.readlines()
        ret = {"start": tmp[0].strip(), "alphabet": {}, "rules": {}}

        for line in tmp[2:]:
            line = line.strip().split(" -> ")
            l, r = line[0], line[1]
            for c in l:
                ret["alphabet"][c] = 0
            ret["alphabet"][r] = 0
            ret["rules"][l] = r
        return ret


def result(inp, part = 1, steps = 10, ret_len = False, ret_state = False):
    res = 0;
    alph = inp["alphabet"]
    rules = inp["rules"]
    state = {k: 0 for k in rules.keys()}

    s = inp["start"]
    for c in s:
        alph[c] += 1

    for i, c in enumerate(s[:-1]):
        state[s[i] + s[i+1]] += 1


    # for k, v in state.items():
    #     if v > 0:
    #         verbose(k)
    
    for _ in range(steps):
        verbose(f"step {_}")
        if _ == 3:
            verbose(sum(alph.values()))
            for k, v in state.items():
                if v > 0:
                    verbose(k, v)
        new_state = {k: 0 for k in rules.keys()}
        for k, v in state.items():
            if v > 0:
                r = rules[k]
                new_state[k[0] + r] += v
                new_state[r + k[1]] += v
                verbose(f"\tadding {r}")
                alph[r] += v
        state = new_state.copy()

    verbose(f"{len(alph) = }")

    res = max(alph.values())- min(alph.values())
    if ret_state:
        return {k: v for k, v in state.items() if v > 0}
    if ret_len:
        return sum(alph.values())
        
    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2, steps = 40))
