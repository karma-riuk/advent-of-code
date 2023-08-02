from queue import PriorityQueue


VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [[int(c) for c in line.strip()] for line in f.readlines()]


def in_bounds(coords, grid):
    x, y = coords
    w, h = len(grid[0]), len(grid)
    return x >= 0 and x < w and y >= 0 and y < h

def result(inp, part = 1):
    if part == 2:
        new_inp = []
        for y in range(5):
            for row in inp:
                new_row = []
                for x in range(5):
                    for c in row:
                        tba = c + x + y 
                        if tba > 9:
                            tba -= 9
                        new_row.append(tba)
                new_inp.append(new_row[:])
        inp = new_inp[:]
    res = 0;
    start = (0, 0)
    end = (len(inp[0]) - 1, len(inp) - 1)

    dists = [[2**30 for _ in range(len(inp[0]))] for _ in range(len(inp))]
    prevs = [[(-1, -1) for _ in range(len(inp[0]))] for _ in range(len(inp))]
    q = PriorityQueue()
    q.put((0, start))
    cur = start
    while cur != end:
        dist, cur = q.get()
        x, y = cur
        verbose(f"looking at {cur = } ({end = })")
        for d in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if in_bounds(d, inp):
                x_, y_ = d
                new_dist = dist + inp[y_][x_]
                if dists[y_][x_] > new_dist:
                    verbose(f"\tlooking at {d = }")
                    prevs[y_][x_] = cur
                    dists[y_][x_] = new_dist
                    q.put((new_dist, d))

    path = set()
    cur = end
    verbose(f"Creating path from {end = }")
    while cur != (0, 0):
        verbose(f"\tlooking at {cur = }")
        path.add(cur)
        cur = prevs[cur[1]][cur[0]]
    path.add(cur)

    for y, row in enumerate(inp):
        for x, c in enumerate(row):
            verbose((BOLD + str(c) + END) if (x, y) in path else c, end='')
        verbose()

    res = dists[end[0]][end[1]]

    return res

BOLD = '\033[95m'
END = '\033[0m'



if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
