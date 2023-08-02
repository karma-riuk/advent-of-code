from math import gcd

def get_input(sample = False):
    with open("sample" if sample else 'input', 'r') as f:
        ret = []
        lines = f.readlines()
        ret.append(int(lines[0]))
        ret.append([int(x) if x != "x" else x for x in lines[1].split(',')])

        return ret

def get_next_bus_departure(bus_id: int, cur_time: int):
    return bus_id * math.ceil(cur_time / bus_id)

def get_result(data: list, part = 1):
    cur_time = data[0]
    busses = data[1]

    if part == 1:
        eta_n_bus = {}
        for bus in busses:
            if bus == 'x': continue
            
            eta = get_next_bus_departure(bus, cur_time)
            eta_n_bus[eta] = bus

        earliest = min(eta_n_bus.keys())
        earliest_bus = eta_n_bus[earliest]
        waiting_time = earliest - cur_time
        return waiting_time * earliest_bus
    else:
        step = busses[0]
        bus_n_offsets = [(bus, offset) for offset, bus in enumerate(busses) if bus != 'x']
        time = 0

        for bus, offset in bus_n_offsets[1:]:
            while True:
                time += step
                if (time + offset) % bus == 0:
                    step = lcm(step, bus)
                    break
        return time
                    
        


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


if __name__ == "__main__":
    print(get_result(get_input(), part = 2))
