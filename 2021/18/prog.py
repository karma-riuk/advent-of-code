VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    import json
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [parse(json.loads(line.strip())) for line in f.readlines()]


class Pair:
    def __init__(self, left, right, parent = None) -> None:
        self.left = left
        self.right = right
        self.parent = parent

    def left_most(self) -> int:
        if isinstance(self.left, int):
            return self.left
        return self.left.left_most()

    def left_most_pair(self):
        if isinstance(self.left, int):
            return self
        return self.left.left_most_pair()

    def right_most(self) -> int:
        if isinstance(self.right, int):
            return self.right
        return self.right.right_most()

    def right_most_pair(self):
        if isinstance(self.right, int):
            return self
        return self.right.right_most_pair()

    def explode(self):
        if not (isinstance(self.left, int) and isinstance(self.left, int)):
            raise ValueError("Both children must be ints to explode")

        cur = self
        while cur.parent != None and cur.parent.left is cur:
            cur = cur.parent
        if cur.parent != None:
            if isinstance(cur.parent.left, int):
                cur.parent.left += self.left
            else:
                cur.parent.left.right_most_pair().right += self.left

        cur = self
        while cur.parent != None and cur.parent.right is cur:
            cur = cur.parent
        if cur.parent != None:
            if isinstance(cur.parent.right, int):
                cur.parent.right += self.right
            else:
                cur.parent.right.left_most_pair().left += self.right

        if self.parent != None:
            if self.parent.left == self:
                self.parent.left = 0
            else:
                self.parent.right = 0

    def split_left(self):
        self.left = Pair(self.left // 2, self.left // 2 + self.left % 2, self)

    def split_right(self):
        self.right = Pair(self.right // 2, self.right // 2 + self.right % 2, self)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"[{str(self.left)}, {str(self.right)}]"

    def __eq__(self, __o) -> bool:
        try:
            return self.left == __o.left and self.right == __o.right
        except Exception as e:
            return False

    def list(self) -> str:
        return [
            self.left if isinstance(self.left, int) else self.left.list(),
            self.right if isinstance(self.right, int) else self.right.list()
        ]

    def __add__(self, __o):
        new = Pair(self, __o)
        self.parent = new
        __o.parent = new
        new.reduce()
        return new

    def reduce(self):
        reduce_again = False
        while True:
            lvl = 0
            old_queue = []
            queue = [self]
            new_queue = []
            while len(queue) != 0 and lvl <= 4:
                lvl += 1
                for n in queue:
                    if not isinstance(n.left, int):
                        new_queue.append(n.left)
                    if not isinstance(n.right, int):
                        new_queue.append(n.right)
                old_queue = queue[:]
                queue = new_queue[:]
                new_queue = []
            queue = old_queue[:]

            if lvl <= 4:
                break
            queue[0].left_most_pair().explode()

            # verbose(f"{lvl = }, {queue = }")
            # if lvl > 4 and len(queue) > 0:
            #     verbose(f"needing to explode some stuff, {queue = }")
            #     reduce_again = True
            #     for n in queue:
            #         n.explode()
            # else:
            #     break

        queue = [self]
        new_queue = []
        while len(queue) != 0:
            lvl += 1
            for n in queue:
                if isinstance(n.left, int):
                    if n.left >= 10:
                        verbose(f"splitting left of {n}")
                        reduce_again = True
                        n.split_left()
                else:
                    new_queue.append(n.left)

                if isinstance(n.right, int):
                    if n.right >= 10:
                        verbose(f"splitting right of {n}")
                        reduce_again = True
                        n.split_right()
                else:
                    new_queue.append(n.right)
            queue = new_queue[:]
            new_queue = []

        if reduce_again:
            self.reduce()

    def mag(self):
        res = 0
        res += 3 * (self.left if isinstance(self.left, int) else self.left.mag())
        res += 2 * (self.right if isinstance(self.right, int) else self.right.mag())
        return res


def parse(arr, parent = None):
    ret = Pair(None, None, parent)
    ret.left = arr[0] if isinstance(arr[0], int) else parse(arr[0], ret)
    ret.right = arr[1] if isinstance(arr[1], int) else parse(arr[1], ret)
    return ret


def result(inp, part = 1, partial = False):
    partial_res = inp[0]
    for p in inp[1:]:
        verbose(f"adding {partial_res} and {p}")
        partial_res += p

    verbose()

    if partial:
        return partial_res
    return partial_res.mag()


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 1))
