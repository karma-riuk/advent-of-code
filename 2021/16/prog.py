VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return int(f.readlines()[0].strip(), 16)


def full_size(packet):
    return 4 * (len(hex(packet)) - 2)

def version(p, size):
    return p >> (size - 3)

def type(p, size):
    return (p >> (size - 6)) & 0b111

def literal(p, size):
    shift = size - 3 - 3 
    res = 0
    while shift >= 0:
        shift -= 5
        res <<= 4
        res |= (p >> shift) & 0xF

        if not ((p >> (shift + 4)) & 1):
            return res
    raise ValueError("couldn't parse literal value correctly")

def type_id(p, size):
    return (p >> (size - 7)) & 1

def len_subpackets(p, size):
    return (p >> (size - 3 - 3 - 1 - 15)) & 0x7FFF

def n_subpackets(p, size):
    return (p >> (size - 3 - 3 - 1 - 11)) & 0x7FF

def parse_packet(p, part = 1, size = -1):
    s = 6
    size = size if size != -1 else full_size(p)
    res = version(p, size)
    t = type(p, size)
    verbose(f"{version(p, size) = }, { type(p, size) = }")
    verbose(format(p, 'b').zfill(size))
    if t == 4:
        verbose(f"\tis literal")
        n = literal(p, size)
        s += 5 * (len(hex(n)) - 2)
        if part == 1:
            return s, version(p, size)
        else:
            return s, n

    tid = type_id(p, size)
    s += 1
    ress = []
    # verbose(f"{tid = }")
    if tid == 0:
        s += 15
        tot_sub_size = len_subpackets(p, size)
        verbose("VVVTTTILLLLLLLLLLLLLLL")
        verbose(f"len of sub packs {tot_sub_size}")


        cur_sub_size = 0
        i = 0
        while cur_sub_size < tot_sub_size:
            verbose(f"scanning for {i = } (reducing {size} by {size - s - tot_sub_size})")
            new_pack = (p >> (size - s - tot_sub_size)) & ((1 << tot_sub_size - cur_sub_size) -1)
            sub_size, sub_res = parse_packet(new_pack, size = tot_sub_size - cur_sub_size, part = part)
            if part == 1:
                res += sub_res
            else:
                ress.append(sub_res)
            cur_sub_size += sub_size
            i += 1
        s += tot_sub_size
    else:
        s += 11
        verbose("VVVTTTILLLLLLLLLLL")
        verbose(f"about to scan {n_subpackets(p, size)} packets")
        for _ in range(n_subpackets(p, size)):
            new_size = size - s
            mask = (1 << new_size) - 1
            new_pack = p & mask
            sub_size, sub_res = parse_packet(new_pack, size = new_size, part = part)
            s += sub_size
            if part == 1:
                res += sub_res
            else:
                ress.append(sub_res)

    if part == 2:
        if t == 0:
            res = sum(ress)
        elif t == 1:
            res = 1
            for r in ress:
                res *= r
        elif t == 2:
            res = min(ress)
        elif t == 3:
            res = max(ress)
        elif t in [5, 6, 7]:
            if len(ress) != 2:
                raise ValueError("huston, we got a problem")
            if t == 5:
                res = int(ress[0] > ress[1])
            elif t == 6:
                res = int(ress[0] < ress[1])
            elif t == 7:
                res = int(ress[0] == ress[1])
                


    return (s, res)

def result(inp, part = 1):
    return parse_packet(inp, part = part)[1]


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))

