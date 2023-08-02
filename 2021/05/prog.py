VERBOSE = True
def verbose(s = "", **kwargs):
    if VERBOSE:
        print(s, **kwargs)

def get_c(s: str):
    c0 = s.split(',')
    return [int(c0[0]), int(c0[1])]

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        tmp = f.readlines()
        ret = {"coords": [], "map_dim": [0, 0]}
        for line in tmp:
            coords = line.split(' -> ')
            c0 = get_c(coords[0])
            c1 = get_c(coords[1])
            ret["coords"].append([c0, c1])
            ret["map_dim"][0] = c0[0] + 1 if c0[0] + 1 > ret["map_dim"][0] else ret["map_dim"][0]
            ret["map_dim"][1] = c0[1] + 1 if c0[1] + 1 > ret["map_dim"][1] else ret["map_dim"][1]
            ret["map_dim"][0] = c1[0] + 1 if c1[0] + 1 > ret["map_dim"][0] else ret["map_dim"][0]
            ret["map_dim"][1] = c1[1] + 1 if c1[1] + 1 > ret["map_dim"][1] else ret["map_dim"][1]

        return ret


def result(inp, part = 1):
    m = [[0 for _ in range(inp["map_dim"][0])] for _ in range(inp["map_dim"][1])]
    for c_pair in inp["coords"]:
        x1, y1 = c_pair[0]
        x2, y2 = c_pair[1]
        if x1 == x2 or y1 == y2 or (part == 2 and abs(x2 - x1) == abs(y2 - y1)):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    m[y][x1] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    m[y1][x] += 1
            elif abs(y1 - y2) == abs(x1 - x2):
                d = (
                    1 if x1 < x2 else -1, 
                    1 if y1 < y2 else -1
                )
                verbose(f"going through {x1, y1 = }, {x2, y2 = } with {d = }")
                x = x1
                y = y1
                m[y][x] += 1
                for _ in range(abs(y2 - y1)):
                    x = x + d[0]
                    y = y + d[1]
                    verbose(f"{x, y = }")
                    m[y][x] += 1
            


    res = 0;
    for row in m:
        for cell in row:
            if cell == 0:
                verbose('.', end='')
            else:
                verbose(cell, end='')
            res += 1 if cell >= 2 else 0

        verbose()
    verbose()

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
