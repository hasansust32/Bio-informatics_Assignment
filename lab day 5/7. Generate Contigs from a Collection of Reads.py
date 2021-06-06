import sys
sys.setrecursionlimit(10000)

patterns = []
with open('rosalind_ba3k.txt') as file:
    lines = file.readlines()
    patterns = [pattern.rstrip() for pattern in lines]


def get_de_bruijn_graph(patterns):
    graph = {}
    incoming = {}
    outgoing = {}
    for pattern in patterns:
        prefix, suffix = pattern[:-1], pattern[1:]

        if prefix not in outgoing:
            outgoing[prefix] = 1
        else:
            outgoing[prefix] += 1

        if suffix not in incoming:
            incoming[suffix] = 1
        else:
            incoming[suffix] += 1

        if prefix not in incoming:
            incoming[prefix] = 0
        if suffix not in outgoing:
            outgoing[suffix] = 0

        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)

    starting_nodes = []
    for key in incoming:
        if incoming[key] == 0 and outgoing[key] != 0:
            starting_nodes.append(key)
    return graph, incoming, outgoing, starting_nodes


def get_contigs(graph, current_path, all_paths, visited):
    current_node = current_path[-1]

    if current_node in visited:
        all_paths.append(current_path)
        return all_paths

    visited.add(current_node)

    if incoming[current_node] > 1:
        all_paths.append(current_path)
        current_path = [current_node]

    if incoming[current_node] > 1 and current_node not in graph:
        return all_paths

    if current_node not in graph:
        all_paths.append(current_path)
        return all_paths

    for node in graph[current_node]:
        temp_path = current_path.copy()
        temp_path.append(node)
        get_contigs(graph, temp_path, all_paths, visited)
    visited.add(current_node)

    return all_paths


def get_maximal_non_branching_paths(graph, incoming, outgoing):
    paths = []
    for node in graph:
        if incoming[node] != 1 or outgoing[node] != 1:
            for outgoing_node in graph[node]:
                current_node = outgoing_node
                non_branching_path = [node, current_node]
                while current_node in graph and incoming[current_node] == 1 and outgoing[current_node] <= 1:
                    current_node = graph[current_node][0]
                    non_branching_path.append(current_node)
                paths.append(non_branching_path)
    return paths


def get_string_from_path(path):
    string = path[0]
    for pattern in path[1:]:
        string += pattern[-1]
    return string


graph, incoming, outgoing, starting_nodes = get_de_bruijn_graph(patterns)
contigs = get_maximal_non_branching_paths(graph, incoming, outgoing)
contigs = [get_string_from_path(contig) for contig in contigs]
output = ' '.join(contigs)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
