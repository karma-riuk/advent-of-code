VERBOSE = True
def verbose(s):
    if VERBOSE:
        print(s)


class Card:
    def __init__(self, width: int, height: int, card: list):
        self.width = width
        self.height = height
        self.marks_h = [0 for _ in range(height)]
        self.marks_v = [0 for _ in range(width)]
        self.won = False # for part 2

        self.numbers = {}
        self.card_h = [[0 for __ in range(width)] for _ in range(height)]
        self.card_v = [[0 for __ in range(height)] for _ in range(width)]

        for y, row in enumerate(card):
            y = int(y)
            for x, n in enumerate(row.strip().replace('  ', ' ').split(' ')):
                x = int(x)
                n = int(n)
                self.numbers[n] = (x, y, False)
                # verbose(f"{x = }, {y = }, {self.card_h = }, {self.card_v = }")
                self.card_h[y][x] = n 
                self.card_v[x][y] = n

    def is_row_full(self, row: int):
        return self.marks_h[row] == 2**self.width - 1

    def is_col_full(self, col: int):
        return self.marks_v[col] == 2**self.height - 1

    def mark(self, n: int):
        if n not in self.numbers:
            return False
        x, y, _ = self.numbers[n]
        self.marks_h[y] |= 1 << (self.width - 1 - x)
        self.marks_v[x] |= 1 << y
        self.numbers[n] = (x, y, True)
        self.won = self.is_row_full(y) or self.is_col_full(x) # for part 2

    def get_winning_sum(self):
        ret = 0
        for n in self.numbers:
            if not self.numbers[n][2]:
                ret += n
        return ret


    def __str__(self):
        ret = ""
        for row in range(self.height):
            for n in self.card_h[row]:
                ret += f"{n:2d} "

            ret += f"     {self.marks_h[row]:05b}"
            ret += "\n"
        return ret

    


def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        lines = f.readlines()
        ret = {}
        ret["draws"] = [int(n) for n in lines[0].split(',')]
        lines = lines[2:]
        ret["cards"] = [Card(5, 5, lines[i:i+5]) for i in range(0, len(lines), 6)]
        return ret


def result(inp, part = 1):
    draws = inp["draws"]
    cards = inp["cards"]

    verbose(f"{len(draws) = }, {len(cards) = }")
    n_won = 0 # for part 2
    for n in draws:
        for c in cards:
            verbose(f"marking {n}")
            if part == 1:
                c.mark(n)
                if c.won:
                    return c.get_winning_sum() * n
            else:
                if not c.won:
                    c.mark(n)
                    if c.won:
                        n_won += 1
                if n_won == len(cards):
                    return c.get_winning_sum() * n
            verbose(c)
    return -1 # failed


if __name__ == "__main__":
    # VERBOSE = False
    print(result(get_input(), part = 2))
