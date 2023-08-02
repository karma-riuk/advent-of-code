def get_input(sample = False):
    with open("sample" if sample else "input", "r") as f:
        return [line.strip() for line in f.readlines()]

def parse_instruction(instruction: str):
    return instruction[:3], int(instruction[4:])

def cmd_n_to_instruction(cmd, n):
    return str(cmd) + " " + (f"+{n}" if n >= 0 else f"{n}")


def instruction_results(cmd, n, i, acc):
    if cmd == "nop":
        return i + 1, acc
    elif cmd == "jmp":
        return i + n, acc
    elif cmd == "acc":
        return i + 1, acc + n


def get_result(instructions: list, part = 1):
    acc = 0
    i = 0

    if part == 1:
        visited = set()
        while i not in visited:
            visited.add(i)

            i, acc = instruction_results(*parse_instruction(instructions[i]), i, acc)
    else:
        history = []
        revert = False
        switched_indices = set()

        while i < len(instructions):
            cmd, n = parse_instruction(instructions[i])

            if i in history:
                revert = True

            if not revert:
                history.append(i)
                i += n if cmd == "jmp" else 1
            else:
                if cmd in ["jmp", "nop"] and i not in switched_indices:
                    instructions[i] = cmd_n_to_instruction("jmp" if cmd == "nop" else "nop", n)
                    switched_indices.add(i)
                    revert = False
                else:
                    i = history[-1]
                    history = history[:-1]

        for i in history:
            cmd, n = parse_instruction(instructions[i])
            if cmd == "acc":
                acc += n

    return acc
    
if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
