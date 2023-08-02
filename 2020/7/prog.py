import re
import json


my_bag = "shiny gold"

def get_input(sample = False, sample_number: int = 1):
    with open("sample_%d" % sample_number if sample else "input", "r") as f:
        return [line.strip() for line in f.readlines()]

def split_n_bags(string: str):
    zero_bags = "no other"

    if string == zero_bags:
        return "", 0

    for i in range(len(string)):
        if string[i] == " ":
            return string[i+1:], int(string[:i])

def parse_input(lines: list):
    ret = {}
    bag_re = re.compile(" ?bags?[ ,.]?")

    for line in lines:
        outer, inner = line.split("contain ")

        outer = bag_re.sub("", outer)
        inner = [bag_re.sub("", x) for x in inner.split(", ")]

        if outer not in ret:
            ret[outer] = {}

        children = {}
        for items in inner:
            bag, n = split_n_bags(items)
            if n != 0:
                children[bag] = n

        if len(children) > 0:
            ret[outer]["children"] = children

        for child in children:
            if child not in ret: ret[child] = {}

            if "parents" not in ret[child]: ret[child]["parents"] = set()
            ret[child]["parents"].add(outer)
    return ret

def fetch_parents_of(child: str, data: dict):
    if "parents" not in data[child]:
        return [child]
    parents = data[child]["parents"]

    parents_total = [child] if child != my_bag else []
    for parent in parents:
        parents_total.extend(fetch_parents_of(parent, data))

    return parents_total

def count_parents_of(child: str, data: dict):
    return len(set(fetch_parents_of(child, data)))

def count_children_of(parent: str, data: dict):
    if "children" not in data[parent]:
        return 0
    children = data[parent]["children"]

    return sum([number + number * count_children_of(child, data) for child, number in children.items()])


def get_result(data: dict, sample: bool = False, part: int = 1):
    if part == 1:
        return count_parents_of(my_bag, data)
    else:
        return count_children_of(my_bag, data)

if __name__ == "__main__":
    print(get_result(parse_input(get_input()), part = 2))
