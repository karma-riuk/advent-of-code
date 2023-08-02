from collections import deque

VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [line.strip() for line in f.readlines()]


def result(inp, part = 1):
    res = 0
    opening = ["(","[", "{", "<"]
    closing = [">", "}" ,"]",  ")"]
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",

    }
    points_1 = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    points_2 = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    tmp_res = []
    for line in inp:
        stack = deque()
        ignore = False
        for c in line:
            if c in opening:
                stack.append(c)
            elif c in closing:
                op = stack.pop()
                if pairs[op] != c:
                    ignore = True
                    if part == 1 :
                        res += points_1[c]
                        break
        if part == 2 and (not ignore) and len(stack) > 0:
            tmp = 0
            verbose("stack before: ", stack, end="")
            while len(stack) > 0:
                tmp *= 5
                tmp += points_2[pairs[stack.pop()]]
            # insert sort
            verbose(" = ", tmp)
            if len(tmp_res) == 0 or tmp > tmp_res[len(tmp_res) - 1]:
                tmp_res.append(tmp)
            else:
                for i, r in enumerate(tmp_res):
                    if tmp < r:
                        tmp_res = tmp_res[:i] + [tmp] + tmp_res[i:]
                        break


    verbose(tmp_res)
    if part == 1:
        return res
    else:
        return tmp_res[len(tmp_res)//2]


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
