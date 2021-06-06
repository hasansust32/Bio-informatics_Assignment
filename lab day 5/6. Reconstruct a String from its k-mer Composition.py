with open('rosalind_ba3h.txt') as file:
    lines = file.readlines()
    k = int(lines[0].rstrip())
    patterns = [pattern.rstrip() for pattern in lines[1:]]


def get_de_bruijn_graph(patterns):
    keys, values = [], []
    graph = {}
    for pattern in patterns:
        prefix, suffix = pattern[:-1], pattern[1:]
        keys.append(prefix)
        values.append(suffix)
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    for key in keys:
        if key not in values:
            first = key
            break
    for value in values:
        if value not in keys:
            last = value
            break
    graph[last] = [first]
    return graph, first, last


def get_hierholzer_cycle(adj_list, start=None):
    if start is None:
        start = next(iter(adj_list))
    stack = [start]
    cycle = []
    while len(stack) > 0:
        current_node = stack[-1]
        while len(adj_list[current_node]) != 0:
            current_node = adj_list[current_node].pop(0)
            stack.append(current_node)
        while len(stack) > 0 and len(adj_list[stack[-1]]) == 0:
            cycle.append(stack.pop())
    cycle.reverse()
    return cycle


def get_string_from_cycle(cycle):
    string = cycle[0]
    for pattern in cycle[1:]:
        string += pattern[-1]
    return string


adjList, first, last = get_de_bruijn_graph(patterns)
cycle = get_hierholzer_cycle(adjList, first)
output = get_string_from_cycle(cycle)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
