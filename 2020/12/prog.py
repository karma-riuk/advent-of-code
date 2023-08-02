def get_input(sample = False):
    with open("sample" if sample else "input") as f:
        return [(line[:1], int(line[1:])) for line in f.readlines()]

def new_dir_after_rotate(cur_dir: str, L_or_R: str, amount: int):
    orientations = ["N", "E", "S", "W"]
    cur_dir_i = orientations.index(cur_dir)
    return orientations[(cur_dir_i + (1 if L_or_R == "R" else -1) * amount // 90) % len(orientations)]

def new_waypoint_after_rotate(cur_wp: list, L_or_R: str, amount: int):
    ret = [0, 0]

    rot = amount // 90 % 4  
    if (rot, L_or_R) == (1, "L") or (rot, L_or_R) == (3, "R"):
        ret[0] = -cur_wp[1]
        ret[1] = cur_wp[0]
    elif rot == 2:
        ret[0] = -cur_wp[0]
        ret[1] = -cur_wp[1]
    elif (rot, L_or_R) == (3, "L") or (rot, L_or_R) == (1, "R"):
        ret[0] = cur_wp[1]
        ret[1] = -cur_wp[0]

    return ret

def get_result(instructions: dict, part = 1):
    position = [0, 0]
    waypoint = [10, 1]
    cur_dir = "E"


    add_to_vertical = lambda dir, x: (1 if dir == "N" else -1) * x
    add_to_horizontal = lambda dir, x: (1 if dir == "E" else -1) * x

    for cmd, amount in instructions:
        if part == 1:
            if cmd == "F":
                if cur_dir in ["N", "S"]:
                    position[1] +=  add_to_vertical(cur_dir, amount)
                elif cur_dir in ["E", "W"]:
                    position[0] +=  add_to_horizontal(cur_dir, amount)
            elif cmd in ["L", "R"]:
                cur_dir = new_dir_after_rotate(cur_dir, cmd, amount)
            elif cmd in ["N", "E", "S", "W"]:
                if cmd in ["N", "S"]:
                    position[1] +=  add_to_vertical(cmd, amount)
                elif cmd in ["E", "W"]:
                    position[0] +=  add_to_horizontal(cmd, amount)
        else:
            if cmd == "F":
                position[0] += waypoint[0] * amount
                position[1] += waypoint[1] * amount
            elif cmd in ["L", "R"]:
                waypoint = new_waypoint_after_rotate(waypoint, cmd, amount)
            elif cmd in ["N", "E", "S", "W"]:
                if cmd in ["N", "S"]:
                    waypoint[1] +=  add_to_vertical(cmd, amount)
                elif cmd in ["E", "W"]:
                    waypoint[0] +=  add_to_horizontal(cmd, amount)

            
    return sum(map(lambda x: abs(x), position))

if __name__ == "__main__":
    print(get_result(get_input(), part = 2))


