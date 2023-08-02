def get_input(sample = False, sample_name = "sample"):
    with open(sample_name if sample else "input", "r") as f:
        return [list(l.strip()) for l in f.readlines()]


def is_there_occupied(range_x, range_y, seats):
    try:
        for x, y in zip(range_x, range_y):
            #  print(f"\tChecking: {x}, {y}")
            if seats[y][x] == "#":
                #  print(f"\tFound an # at {x}, {y}")
                return True
            elif seats[y][x] == "L":
                return False
        return False
    except IndexError:
        return False

    

def count_occupied_direction(center_x, center_y, seats):
    count = 0
    len_x = len(seats[0])
    len_y = len(seats)
    
    directions = [
            ( # N
                [center_x] * center_y, 
                range(center_y - 1, -1, -1)
                ), 
            ( # NE
                range(center_x + 1, len_x),
                range(center_y - 1, -1, -1)
                ), 
            ( # E
                range(center_x + 1, len_x),
                [center_y] * (len_x - center_x)
                ),
            ( # SE
                range(center_x + 1, len_x),
                range(center_y + 1, len_y)
                ),
            ( # S
                [center_x] * (len_y - center_y), 
                range(center_y + 1, len_y)
                ),
            ( # SW
                range(center_x - 1, -1, -1),
                range(center_y + 1, len_y)
                ),
            ( # W
                range(center_x - 1, -1, -1),
                [center_y] * center_x
                ),
            ( # NW
                range(center_x - 1, -1, -1),
                range(center_y - 1, -1, -1),
                ) 
            ]

    for range_x, range_y in directions:
        if is_there_occupied(range_x, range_y, seats):
            count += 1

    return count

def count_occupied_around(center_x, center_y, seats):
    count = 0
    len_x = len(seats[0])
    len_y = len(seats)

    for y in range(center_y-1, center_y+2):
        for x in range(center_x-1, center_x+2):

            if x in range(len_x) and y in range(len_y) and (x, y) != (center_x, center_y):
                if seats[y][x] == "#" : count += 1

    return count


def get_dummy_seats(len_x, len_y):
    ret = []
    for y in range(len_y):
        line = ""
        for x in range(len_x):
            line += "."
        ret.append(line)
    return ret

def get_result(seats: list, part = 1):
    len_x = len(seats[0])
    len_y = len(seats)
    prev_seats = get_dummy_seats(len_x, len_y)

    while prev_seats != seats:
        new_seats = [[item for item in line] for line in seats]
        for y in range(len_y):
            for x in range(len_x):
                place = seats[y][x]
                if place == ".": continue
                count = count_occupied_around(x, y, seats) if part == 1 else count_occupied_direction(x, y, seats)

                if place == "L" and count == 0:
                    new_seats[y][x] = "#"
                elif place == "#" and count >= (4 if part == 1 else 5):
                    new_seats[y][x] = "L"

        prev_seats = seats
        seats = new_seats

    count = 0
    for line in seats:
        for char in line:
            if char == "#": count += 1
    return count
        
if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
