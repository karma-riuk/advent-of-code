import re

def get_input(sample = False, sample_n = 1):
    with open(f"sample_{sample_n}" if sample else 'input', 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse_val_masks(mask: str):
    mask_0 = 0
    mask_1 = 0
    for c in mask:
        if c == "X":
            mask_0 = (mask_0 << 1) + 1
            mask_1 = mask_1 << 1
        elif c == "0":
            mask_0 = mask_0 << 1 
            mask_1 = mask_1 << 1
        elif c == "1":
            mask_0 = (mask_0 << 1) + 1
            mask_1 = (mask_1 << 1) + 1

    return mask_0, mask_1

def masked_value(value: int, masks: tuple):
    return (value & masks[0]) | masks[1]

def decode_memory_address(address: int, mask: str):
    ret = {address}
    for i, c in enumerate(mask):
        shift_amount = len(mask) - 1 - i
        if c in ['1', 'X']:
            new_ret = set()
            for addr in ret:
                if c == '1':
                    new_ret.add(addr | (1 << shift_amount))
                elif c == 'X':
                    new_ret.update((addr | (1 << shift_amount), addr & ~(1 << shift_amount)))
            ret = new_ret
    return ret



def get_result(instructions: list, part = 1):
    mem_re = re.compile(r'^mem\[(\d+)\] = (\d+)$')
    mask_re = re.compile(r'^mask = ([X10]{36})$')
    mem = {}
    val_masks = (0, 0)
    mem_masks = ""

    for cmd in instructions:
        if match := mem_re.match(cmd):
            index, value = (int(x) for x in match.groups())

            indexes = {index} if part == 1 else decode_memory_address(index, mem_mask)
            for i in indexes:
                mem[i] = masked_value(value, val_masks) if part == 1 else value

        elif match := mask_re.match(cmd):
            val_masks = parse_val_masks(*match.groups())
            mem_mask = match.groups()[0]

        else:
            raise ValueError(f"The instruction `{cmd}` is not valid") 

    return sum(mem.values())

if __name__ == "__main__":
    print(get_result(get_input(), part = 2))

