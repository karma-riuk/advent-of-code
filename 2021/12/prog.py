VERBOSE = True
def verbose(s = "", *args, **kwargs):
    if VERBOSE:
        print(s, *args, **kwargs)

def get_input(sample = False, part = 1):
    with open(f'sample_p{part}' if sample else 'input', 'r') as f:
        return [line.strip() for line in f.readlines()]



def dfs(start, end, I_V, E, visited, path, part):
    verbose(f"\t\tvisiting {I_V[start]} ({part = })")
    if start == end:
        verbose(f"found end")
        verbose(f"\t\tpath {list(map(lambda i: I_V[i], path))}")
        verbose("\t\t", end = "")
        for i, v in enumerate(visited):
            if v:
                verbose(f"{I_V[i]} visted {v}, ", end = "")
        verbose()
        return 1
    ret = 0 
    for i, e in enumerate(E[start]):
        if e > 0 and visited[i] < part and visited.count(2) <= 2 :
            tmp_v = visited[:]
            if I_V[i] == I_V[i].lower():
                tmp_v[i] += 1
            # verbose(f"\tstarting search from {I_V[i]}")
            ret += dfs(i, end, I_V, E, tmp_v[:], path + [i], part)
    return ret

def result(inp, part = 1):
    res = 0;
    # construct the graph with an adjacency matrix
    V_I = {}
    I_V = []
    for line in inp:
        nodes = line.split('-')
        for n in nodes:
            if n not in V_I:
                V_I[n] = len(I_V)
                I_V.append(n)

    E = [[0 for _ in range(len(V_I))] for _ in range(len(V_I))]

    for line in inp:
        nodes = line.split('-')
        n1, n2 = V_I[nodes[0]], V_I[nodes[1]]
        E[n1][n2] += 1
        E[n2][n1] += 1

    start = V_I["start"]
    verbose(f"{start = }")
    end = V_I["end"]
    verbose(f"{end = }")
    visited = [0] * len(V_I)
    visited[start] = 2

    res = dfs(start, end, I_V, E, visited, [start], part)

    return res


if __name__ == "__main__":
    VERBOSE = False
    print(result(get_input(), part = 2))
