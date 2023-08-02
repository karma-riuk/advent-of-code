VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [[int(i) for i in line.strip()] for line in f.readlines()]


def result(inp, part = 1, steps = 100, grid = False):
    res = 0;
    for step in range(1, steps+1 if part == 1 else 2**31 - 1):
        # increment each octopus
        inp = [[i+1 for i in line] for line in inp]
        # get the ones about to flash
        queue = []
        idx = 0
        for y, row in enumerate(inp):
            for x, cell in enumerate(row):
                if cell > 9:
                    queue.append((x, y))

        while idx < len(queue):
            res += 1
            x, y = queue[idx]
            idx += 1
            inp[y][x] = 0
            for d in [(x-1, y-1), (x, y-1), (x+1, y-1),
                      (x-1, y),             (x+1, y),
                      (x-1, y+1), (x, y+1), (x+1, y+1)]:
                x1, y1 = d
                if x1 < 0 or x1 >= len(inp[0]) or y1 < 0 or y1 >= len(inp):
                    continue
                if d not in queue:
                    inp[y1][x1] += 1
                    if inp[y1][x1] > 9:
                        queue.append(d)

        if step in [193, 194, 195]:
            verbose(f"{step = }")
            verbose(f"{len(queue) = }")
            for row in inp:
                verbose(str(row))

        if part == 2 and len(queue) == len(inp) * len(inp[0]):
            return step

    verbose(f"{len(queue) = }")
    for row in inp:
        verbose(str(row))
    if grid:
        return inp
    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
