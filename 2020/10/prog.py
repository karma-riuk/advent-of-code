def get_input(sample = False, number = 1):
    with open(f"sample_{number}" if sample else "input", 'r') as f:
        return [int(i) for i in f.readlines()]

def get_result(data: list, part = 1):
    data.sort()
    data = [0] + data + [data[-1] + 3]
    diffs = []

    for i in range(len(data) - 1):
        n1, n2 = data[i], data[i + 1]
        diffs.append(n2 - n1)

    if part == 1:
        return diffs.count(1) * diffs.count(3)
    else:
        for diff in diffs
        return 0


if __name__ == "__main__":
    print(get_result(get_input()))

