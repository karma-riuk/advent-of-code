import re

def extract_passports(passports: list):
    ret = []
    kv_re = re.compile(r'(\w+):(#?\w+)')

    for passport in passports:
        dic = {}
        for key, val in kv_re.findall(passport):
            dic[key] = val
        ret.append(dic)
            
    return ret


def get_input(sample = False):
    with open("sample" if sample else "input", "r") as f:
        content = f.read()
        passports = content.split("\n\n")
        return extract_passports(passports)

def is_passport_valid_1(passport: dict):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    keys = set(passport.keys())
    return keys == fields or keys == fields | {"cid"}

between = lambda m1, x, m2: int(m1) <= int(x) and int(x) <= int(m2);

def is_height_valid(height: str):
    h_re = re.compile(r'^(\d+)(cm|in)$')
    if h_re.match(height) == None: return False

    number, measure = h_re.findall(height)[0]

    return (measure == "cm" and between(150, number, 193)) or (measure == "in" and between(59, number, 76))


def is_passport_valid_2(passport: dict):
    is_four_digits = lambda x: re.match(r'^\d{4}$', x) != None

    rules = {"byr": lambda x: is_four_digits(x) and between(1920, x, 2002),
            "iyr": lambda x: is_four_digits(x) and between(2010, x, 2020),
            "eyr": lambda x: is_four_digits(x) and between(2020, x, 2030),
            "hgt": is_height_valid,
            "hcl": lambda x: re.match(r'^#[a-f0-9]{6}$', x) != None,
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda x: re.match(r'^\d{9}$', x) != None,
            "cid": lambda x: True} 

    #  try:
    #      print(passport["hcl"], rules["hcl"](passport["hcl"]))
    #  except KeyError as e:
    #      pass

    for key, val in passport.items():
        if not rules[key](val):
            return False
    return True

def get_result(passports: list, part = 1):
    ret = 0
    print(f"{len(passports)=}")
    for p in passports:
        if (part == 1 and is_passport_valid_1(p)) or (part == 2 and is_passport_valid_2(p) and is_passport_valid_1(p)):
            ret += 1
    return ret


def main(sample = False, part = 1):
    inp = get_input(sample = sample)
    res = get_result(inp, part = part)

    if sample:
        expected = 2 if part == 2 else 0
        print(f"{res=}")
        print(res == expected)
    else:
        print(res)

    
main(sample = False, part = 2)
