VERBOSE = False

def get_input(sample = False, part = 1):
    global n_bits
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        tmp = f.readlines()
        n_bits = len(tmp[0]) - 1
        return [int(line.strip(), 2) for line in tmp]

def verbose(s):
    if VERBOSE:
        print(s)


def filter_by(most, inp):
    global n_bits
    for i in range(n_bits - 1, -1, -1):
        dic = {0: [], 1: []}
        for n in inp:
            dic[(n >> i) & 1].append(n)

        verbose(dic)
        if len(dic[1]) >= len(dic[0]):
            inp = dic[1 if most else 0][:]
        else:
            inp = dic[0 if most else 1][:]

        if len(inp) == 1:
            return inp[0]
    
def result(inp, part = 1):
    global n_bits
    if part == 1:
        # print(n_bits)
        tot = len(inp)
        gamma = eps = 0
        for i in range(n_bits):
            ones = 0
            for n in inp:
                ones += (n >> i) & 1

            a = 1 if ones > tot/2 else 0
            gamma |= a << i

        eps = (2**n_bits - 1) ^ gamma
        return eps * gamma
    else:
        ox = filter_by(True, inp)
        co = filter_by(False, inp)
        verbose(f"{ox = }, {co = }")
        return ox * co


if __name__ == "__main__":
    print(result(get_input(), part = 2))
