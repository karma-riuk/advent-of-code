import re
calc_re = re.compile(r'(\d+) ([+*]) (\d+)')

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_closing_bracket_starting_at(index: int, string: str):
    open_br = 0
    for i, c in enumerate(string[index:], start=index):
        if c == "(":
            open_br += 1
        elif c == ")":
            open_br -= 1
        if open_br == 0:
            return i

def evaluate_advanced(calc: str):
    starting_bracket = calc.find("(")
    if starting_bracket != -1:
        end_bracket = find_closing_bracket_starting_at(starting_bracket, calc)
        return evaluate_advanced(calc[:starting_bracket] + str(evaluate_advanced(calc[starting_bracket+1:end_bracket])) + calc[end_bracket+1:])
    
    additions = [external_group for external_group, internal_group in re.findall(r'((\d+ \+ )+\d+)', calc)]
    for add in additions:
        calc = calc.replace(add, str(eval(add)), 1)
    return eval(calc)
    


def evaluate_l2r(calc: str):
    starting_bracket = calc.find("(")
    if starting_bracket != -1:
        end_bracket = find_closing_bracket_starting_at(starting_bracket, calc)
        return evaluate_l2r(calc[:starting_bracket] + str(evaluate_l2r(calc[starting_bracket+1:end_bracket])) + calc[end_bracket+1:])

    match = calc_re.match(calc)

    first, operation, second = match.groups()
    first, second = int(first), int(second)

    rest = calc[match.end():]
    if operation == "+":
        new = first + second
    elif operation == "*":
        new = first * second
    
    return new if len(rest) == 0 else evaluate_l2r(str(new) + rest)


def get_result(inp: list, part = 1):
    return sum((evaluate_l2r(op) if part == 1 else evaluate_advanced(op)) for op in inp)

if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
