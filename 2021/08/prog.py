VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        ret = []
        for line in f.readlines():
            parts = line.strip().split('|')
            ret.append({
                "ref": parts[0].strip().split(' '),
                "out": parts[1].strip().split(' ')
            })
        return ret


def result(inp, part = 1):
    res = 0;
    if part == 1:
        for data in inp:
            for s in data["out"]:
                verbose(s)
                if len(s) in [2, 3, 4, 7]:
                    res += 1
    else:
        for data in inp:
            for s in data["ref"]:
                s = list(s)
                l = len(s)
                if l == 2: 
                    one = s[:]
                elif l == 3:
                    seven = s[:]
                elif l == 4:
                    four = s[:]
                elif l == 7: 
                    eight = s[:]
            a = list(filter(lambda x: x not in one, seven))[0]
                    

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 1))
