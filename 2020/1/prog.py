def get_file_input(filename):
    ret = set()
    with open("input", "r") as f:
        for i, line in enumerate(f.readlines()):
            if " " in line:
                raise ValueError(f"Only on value can be put per line in the input file (space detected at line {i} the input file).")
            ret.add(int(line))
    return ret

def get_2_numbers(s: set):
    goal = 2020

    known = set()
    for e in s:
        sub_goal = 2020 - e
        if sub_goal in known:
            return e, sub_goal
        known.add(e)


def init_dict(s: set):
    ret = dict()
    for e in s:
        ret[e] = {e}
    return ret 


def get_n_numbers(n_entries: int, s: set, data: dict):
    if data == {}:
        data = init_dict(s)

    if n_entries == 2:
        goal = 2020

        for e in s:
            sub_goal = 2020 - e
            if sub_goal in data.keys():
                return e, *data[sub_goal]
    else:
        new_data = {}
        for e in s:
            for result, values in data.items():
                if e in values: pass
                new_data[result + e] = values | {e}
        return get_n_numbers(n_entries - 1, s, new_data)

def get_result(*ns: int):
    ret = 1
    for n in ns:
        ret *= n
    return ret

def main(n_entries = 2, use_sample_input = True):
    sample = { 1721,
            979,
            366,
            299,
            675,
            1456}
    
    res = get_result(
            *get_n_numbers(
                n_entries, 
                sample if use_sample_input else get_file_input("input"), 
                {})
            )

    if use_sample_input:
        expected = 241861950 if n_entries == 3 else 514579 # if n_entries == 2 
        return f"{res} {res==expected}".upper()
    else:
        return res


print(main(n_entries = 3, use_sample_input = False))
