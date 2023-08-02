VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)


def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        tmp = f.readlines()
        coords = []
        n = -1
        for i, line in enumerate(tmp):
            line = line.strip()
            if line == "":
                n = i+1
                break
            line = line.split(",")
            coords.append((int(line[0]), int(line[1])))

        folds = []

        for fold in tmp[n:]:
            fold = fold[11:]
            fold = fold.split("=")
            folds.append((fold[0], int(fold[1])))

        return {
            "coords": set(coords),
            "folds": folds
        }


def width(l):
    m = 0
    for x, _ in l:
        if m < x:
            m = x
    return m + 1

def height(l):
    m = 0
    for _, y in l:
        if m < y:
            m = y
    return m + 1

def print_grid(coords, w, h):
    out = [[" " for _ in range(w)] for _ in range(h)]
    for x, y in coords:
        verbose(f"{x, y = }, {w, h = }")
        out[y][x] = '#'
    for l in out:
        print(''.join(l))


def result(inp, part = 1):
    res = 0;
    coords = inp["coords"]
    w = width(coords)
    h = height(coords)
    for axis, n in inp["folds"]:
        new_coords = []
        verbose(f"folding over {axis} = {n}")
        # verbose(f"\tbefore {coords = }")
        # print_grid(coords, w, h)
        for x, y in coords:
            nc = (x, y)
            verbose(f"\tbefore {nc}")
            if axis == "x" and  x >= n:
                nc = (w - 1 - x, y)
            elif axis == "y" and y >= n:
                nc = (x, h - 1 - y)
            verbose(f"\tafter {nc}")
            new_coords.append(nc)
        if axis == 'x': w = n
        else: h = n
        coords = list(set(new_coords))
        # verbose(f"\tafter {coords = }")
        # print_grid(coords, width(coords), height(coords))
        if part == 1:
            return len(coords)


    print_grid(coords, w, h)

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
