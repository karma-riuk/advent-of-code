def get_input(sample = False):
    with open('sample' if sample else 'input', 'r') as f:
        ret = {0: {0: {}}}
        lines = f.readlines()
        for y, row in enumerate(lines, start = -len(lines) // 2):
            ret[0][0][y] = {}
            row = row.strip()
            for x, cube in enumerate(row, start = -len(row) // 2):
                ret[0][0][y][x] = cube
        return ret

def count_actives(space: dict):
    ret = 0
    for w in space.values():
        for z in w.values():
            for y in z.values():
                for x in y.values():
                    if x == "#":
                        ret += 1
    return ret

def count_active_neighbours(space: dict, center_x, center_y, center_z, center_w):
    ret = 0
    for w in range(center_w - 1, center_w + 2):
        if w not in space.keys(): continue
        for z in range(center_z - 1, center_z + 2):
            if z not in space[w].keys(): continue
            for y in range(center_y - 1, center_y + 2): 
                if y not in space[w][z].keys(): continue
                for x in range(center_x - 1, center_x + 2):
                    if x in space[w][z][y].keys() and (x, y, z, w) != (center_x, center_y, center_z, center_w) and space[w][z][y][x] == "#":
                        ret += 1
    return ret


def print_space(space: dict):
    for w, time in sorted(space.items()):
        for z, plain in sorted(space[w].items()):
            print(f"\t{z = } {w = }")
            for y, row in sorted(plain.items()):
                print(f"\t{''.join([value for key, value in sorted(row.items())])}")
            print()




def get_result(space_4d: list, part = 1):
    for cycle in range(6):
        next_space_4d = {}
        for w in range(min(space_4d) - 1, max(space_4d) + 2) if part == 2 else [0]:
            space = space_4d[w] if w in space_4d else {z_0 : {y_0: {x_0: '.' for x_0 in space_4d[0][0][0]} for y_0 in space_4d[0][0]} for z_0 in space_4d[0]}
            next_space_4d[w] = {}
            for z in range(min(space) - 1, max(space) + 2):
                plain = space[z] if z in space else {y_0: {x_0: '.' for x_0 in space[0][0]} for y_0 in space[0]}
                next_space_4d[w][z] = {}

                for y in range(min(plain) - 1, max(plain) + 2):
                    row = plain[y] if y in plain else {x_0: '.' for x_0 in space[0][0]}
                    next_space_4d[w][z][y] = {}

                    for x in range(min(row) - 1, max(row) + 2):
                        cube = row[x] if x in row else '.'
                        count = count_active_neighbours(space_4d, x, y, z, w)
                        if cube == "#":
                            if count in [2, 3]:
                                next_cube = "#"
                            else:
                                next_cube = "."
                        else:
                            if count == 3:
                                next_cube = "#"
                            else:
                                next_cube = "."
                        next_space_4d[w][z][y][x] = next_cube
        space_4d = next_space_4d

    return count_actives(space_4d)


if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
