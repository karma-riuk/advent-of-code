import math, re
VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        m = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", f.readlines()[0])
        return tuple(map(lambda x: int(x), m.groups()))



def v_x(t, v0):
    return max(-t + v0, 0)

def v_y(t, v0):
    return -t + v0


def result(inp, part = 1):
    y = abs(min(inp[2], inp[3])) - 1
    v_y_max = int(y*(y+1) / 2);
    if part == 1:
        return v_y_max

    x_2 = math.ceil((-1 + math.sqrt(1 - 4 * (-2) * inp[1])) / 2)
    x_1 = math.ceil((-1 + math.sqrt(1 - 4 * (-2) * inp[0])) / 2)
    x_min = inp[0]
    x_max = inp[1]
    y_min = inp[2]
    y_max = inp[3]

    global VERBOSE

    res = 0
    for v0x in range(x_1, x_max+1):
        for v0y in range(y_min, v_y_max+1):
            verbose(f"{v0x, v0y}", end = " ")
            t = 0
            y = 0
            x = 0
            while y >= y_min:
                y += v_y(t, v0y)
                x += v_x(t, v0x)
                # verbose(f"\t{x, y = }")
                if x_min <= x and x <= x_max and y_min <= y and y <= y_max:
                    verbose(f"accepted", end='')
                    res += 1
                    break
                t += 1
            verbose("")

    # x = inp[1] - inp[0]
    # x += x2 - x1 + 1
    # verbose(f"{x1, x2 = }")
    # y = abs(inp[3]) - abs(inp[2])
    # y +=  v_y_max
    return res


if __name__ == "__main__":
    VERBOSE = not False
    print(result(get_input(), part = 2))
