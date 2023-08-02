import math

VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [[int(c) for c in line.strip()] for line in f.readlines()]


def result(inp, part = 1):
    res = 0;
    width = len(inp[0])
    height = len(inp)
    lowest_h = [0 for _ in range(height)]
    lowest_v = [0 for _ in range(height)]
    lowest = [0 for _ in range(height)]

    # get lowest in horizontal
    for y, row in enumerate(inp):
        for x, cell in enumerate(row):
            if (x == 0 and cell < row[x+1]) \
                    or (x == width - 1 and cell < row[x-1]) \
                    or (cell < row[x-1] and cell < row[x+1]):
                lowest_h[y] |= 1 << (width - x)

    # get lowest in vertical
    for x in range(width):
        for y in range(height):
            row = inp[y]
            cell = row[x]
            if (y == 0 and cell < inp[y+1][x]) \
                    or (y == height - 1 and cell < inp[y-1][x]) \
                    or (cell < inp[y-1][x] and cell < inp[y+1][x]):
                lowest_v[y] |= 1 << (width - x)

    # combine both lowests and get the overall lowests
    for y in range(height):
        lowest[y] = lowest_h[y] & lowest_v[y]


    lowest_points = []
    for y, row in enumerate(inp):
        for x, cell in enumerate(row):
            if lowest[y] >> (width - x) & 1 == 1:
                if part == 1:
                    res += cell + 1
                else:
                    lowest_points.append((x, y))

    if part == 1:
        return res

    res = 1
    verbose(lowest_points)
    basins = []
    for point in lowest_points:
        queue = [point]
        idx = 0
        while idx < len(queue):
            x, y = queue[idx]
            for d in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if d[0] >= 0 and d[0] < width and d[1] >= 0 and d[1] < height \
                        and d not in queue and inp[d[1]][d[0]] != 9:
                    queue.append(d)

            idx += 1;
        verbose(f"From { point =  }, the region is {len(queue)}")
        basins.append(len(queue))

    basins.sort()
    res = math.prod(basins[-3:])

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
