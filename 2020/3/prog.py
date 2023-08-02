def get_file_input(filename: str):
    ret = []
    with open(filename, "r") as f:
        for line in f.readlines():
            ret.append(line.strip())
    return ret

def main(use_sample_input = True, part = 1): 
    sample = [ 
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
            ]
    
    s = sample if use_sample_input else get_file_input("input")

    if part == 1:
        expected_result = 7
        res = get_result(s, 3, 1)
    else:
        expected_result = 336
        slopes = {
                (1, 1),
                (3, 1),
                (5, 1),
                (7, 1),
                (1, 2)
                }

        tmp = []
        for slope in slopes:
            tmp.append(get_result(s, *slope))

        res = mult_all(*tmp)

    if use_sample_input:
        return f"{res} {res==expected_result}".upper()
    else:
        return res

def mult_all(*ns: int):
    ret = 1
    for n in ns:
        ret *= n
    return ret

def get_result(l: list, inc_x: int, inc_y: int):
    ret = 0
    x = 0
    y = 0
    while y < len(l):
        if l[y][x] == "#":
            ret += 1
        x += inc_x
        x %= len(l[0])
        y += inc_y
    return ret

print(main(use_sample_input = False, part = 2))


