def get_file_input(filename: str):
    ret = set()
    with open(filename, "r") as f:
        for line in f.readlines():
            rule, *pwd = line.split(":")
            pwd = "".join(pwd).strip()
            ret.add((pwd, rule))
    return ret

def main(use_sample_input = True):
    sample = {
             ("abcde", "1-3 a"),
             ("cdefg", "1-3 b"),
             ("ccccccccc", "2-9 c"),
            }
    expected_result = 2

    res = get_result(sample if use_sample_input else get_file_input("input"))

    if use_sample_input:
        return f"{res} {res==expected_result}"
    else:
        return res

def check_n_chars(pwd: str, char: str, n_min: int, n_max: int) -> bool: # part 1
    n = 0 
    for c in pwd:
        if c == char:
            n += 1
    return n_min <= n and n <= n_max

def check_pos_chars(pwd:str, char: str, pos1: int, pos2: int) -> bool: # part 2
    return (pwd[pos1] == char) != (pwd[pos2] == char)


def is_pwd_ok(pwd: str, rule: str) -> bool:
    *delimiters, char = rule.split(" ")
    n_min, n_max = "".join(delimiters).split("-")
    n_min = int(n_min)
    n_max = int(n_max)

    return check_pos_chars(pwd, char, n_min - 1, n_max - 1)


def get_result(data: dict) -> int:
    ret = 0
    for pwd, rule in data:
        b = is_pwd_ok(pwd, rule)
        ret += 1 if b else 0

    return ret

    

print(main(use_sample_input = False))

