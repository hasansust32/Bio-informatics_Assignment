adjList = {}
with open('rosalind_ba3f.txt') as file:
    while True:
        line = file.readline().rstrip()
        if line is None or line == '':
            break
        key = int(line.split('->')[0].rstrip())
        values = line.split('->')[1].rstrip().split(',')
        values = [int(value.rstrip()) for value in values]
        adjList[key] = values


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


cycle = get_hierholzer_cycle(adjList)
output = '->'.join([str(node) for node in cycle])
print(output)
with open('output.txt', 'w') as file:
    file.write(output)

