from yaml import dump
def get_result(inp: list, part = 1):
    last_pos = {n: i+1 for i, n in enumerate(inp[:-1])}
    prev_item = inp[-1]
    for i in range(len(inp), 2020 if part == 1 else 30_000_000):
        cur_item = 0 if prev_item not in last_pos.keys() else i - last_pos[prev_item]
        last_pos[prev_item] = i
        prev_item = cur_item

    return cur_item

if __name__ == "__main__":
    print(get_result([20, 9, 11, 0, 1, 2], part = 2))

