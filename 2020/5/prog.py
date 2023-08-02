def get_input(sample = False):
    filename = "sample" if sample else "input"
    with open(filename + ".prod", "r") as f:
        return [line.strip() for line in f.readlines()]

def char_to_bin(char: str):
    if char not in ["F", "B", "L", "R"]:
        raise ValueError(f"Character `{char=}` cannot be transformed into binary")
    return 0 if char == "F" or char == "L" else 1

def seat_to_bin(seat: str):
    if len(seat) == 1:
        return char_to_bin(seat)
    return char_to_bin(seat[0])*2**(len(seat)-1) + seat_to_bin(seat[1:])

def seats_to_binary_list(seats: list):
    return [seat_to_bin(seat) for seat in seats]


def get_result(seats: list, part = 1):
    if part == 1:
        return max(seats)
    else:
        candidates = []
        seats.sort()

        prev = seats[0]
        for i in range(1, len(seats)):
            next = seats[i]
            if prev + 2 == next:
                candidates.append(prev + 1)
            prev = next
        return candidates


    

def main(sample = False, part = 1):
    inp = seats_to_binary_list(
            get_input(sample = sample)
            )
    return get_result(inp, part=part) 

print(main(part = 2))



