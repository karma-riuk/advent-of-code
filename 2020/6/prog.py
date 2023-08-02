def get_input(sample = False):
    ret = []
    with open("sample" if sample else "input", "r") as f:
       group = [] 
       for line in f.readlines():
           if line == "\n": # empty line
               ret.append(group)
               group = []
           else:
               group.append(line.strip())
       ret.append(group) # add last group
       return ret

def list_of_string_to_list(s: set):
    ret = []
    for string in s:
        ret += list(string)
    return ret

def grouped_answers(answers: list):
    ret = []
    start_i = 0
    prev = answers[start_i]
    for cur_i in range(1, len(answers)):
        cur = answers[cur_i]
        if prev != cur:
            ret.append(answers[start_i:cur_i])
            start_i = cur_i
        prev = cur
    ret.append(answers[start_i:]) # add last answer
    return ret

def list_of_string_to_set(s: set):
    ret = set()
    for string in s:
        ret |= set(string)
    return ret

def get_result(inp: list, part = 1):
    ret = 0
    for group in inp:
        if part == 1:
            ret += len(list_of_string_to_set(group))
        else:
            group_len = len(group)
            splitted_answers = list_of_string_to_list(group)
            splitted_answers.sort()
            ga = grouped_answers(splitted_answers)
            ret += sum(map(lambda x: int(len(x) == group_len), ga))


    return ret




if __name__ == "__main__":
    print(get_result(get_input(), part = 2))



