import re

#################################################################################
#                                                                               #
#  DISCLAIMER: THE SOLUTION I FOUND THE THIS DAY IS HORRIBLE, I AIN'T PROUD OF  #
#  IT AT ALL (IT WORKS THO)                                                     #
#                                                                               #
#################################################################################


def get_input(sample = False, part = 1):
    with open(f"sample_p{part}" if sample else "input", "r") as f:
        ret = {}
        data = f.read().split("\n\n")
        ranges = {}
        for line in data[0].split("\n"):
            name, range = get_range(line)
            ranges[name] = range

        ret["ranges"] = ranges
        ret["my ticket"] = [int(v) for v in data[1].split("\n")[1].split(",")]
        ret["nearby tickets"] = [[int(v) for v in line.split(",")] for line in data[2].split("\n")[1:]]
        return ret

        
def get_range(range_str: str):
    range_re = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
    name, min_1, max_1, min_2, max_2 = range_re.match(range_str).groups()
    return name, [range(int(min_1), int(max_1) + 1), range(int(min_2), int(max_2) + 1)]


def get_result(inp: dict, part = 1):
    invalid_values = []
    invalid_ticket_indices = set()
    for i_ticket, ticket in enumerate(inp["nearby tickets"]):
        for value in ticket:
            is_value_valid = False
            for r in inp["ranges"].values():
                if value in r[0] or value in r[1]:
                    is_value_valid = True
                    break

            if not is_value_valid:
                invalid_values.append(int(value))
                invalid_ticket_indices.add(i_ticket)
            
    if part == 1:
        return sum(invalid_values)

    valid_tickets = [ticket for i, ticket in enumerate(inp['nearby tickets']) if i not in invalid_ticket_indices]

    range_to_index = {name: {i for i in range(len(valid_tickets[0]))} for name in inp["ranges"]}

    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            for name, rng in inp["ranges"].items():
                if not (value in rng[0] or value in rng[1]):
                    range_to_index[name].discard(i)

    # I'M SO SORRY FOR THIS WHILE LOOP, BUT I FOUND NO OTHER WAY TO "MUTUALLY EXCLUDE" EVERY SET OF INDICES FROM ONE ANOTHER... :/
    while list(map(lambda x: len(x), range_to_index.values())) != [1]*len(range_to_index):
        for name, indices in range_to_index.items():
            if len(indices) == 1:
                for i_name, i_indices in range_to_index.items():
                    if name != i_name:
                        range_to_index[i_name] = i_indices - indices

    re_dep = re.compile(r'^departure ')
    ret = 1 
    for name, index in range_to_index.items():
        if re_dep.match(name) != None:
            ret *= inp["my ticket"][index.pop()]

    return ret

if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
