with open('rosalind_ba9a.txt') as file:
    pattern_list = [pattern.rstrip() for pattern in file.readlines()]


class Node:
    def __init__(self, val=None, pos=0):
        self.pos = pos
        self.val = val
        self.children_list = set()

    def add_children(self, node):
        self.children_list.add(node)

    def get_children(self, val):
        children = None
        for node in self.children_list:
            if node.val == val:
                children = node
        return children


    def __str__(self):
        if self.val == Node:
            display_text = 'None'
        else:
            display_text = str(self.val)
        children_text = ''
        for child in self.children_list:
            children_text += str(child.val) + ' '
        display_text = f'val: {display_text}, children: {children_text}'
        return display_text


root = Node()
adj_list = []
current_len = 0
for pattern in pattern_list:
    current_node = root
    for symbol in pattern:
        child_node = current_node.get_children(symbol)
        if child_node is None:
            current_len += 1
            child_node = Node(symbol, current_len)
            current_node.add_children(child_node)
            adj_list.append((current_node.pos, current_len, symbol))
        current_node = child_node

adj_list.sort(key=lambda x: (x[0], x[1]))
output = ''
for item in adj_list:
    output += f'{item[0]}->{item[1]}:{item[2]}\n'
output = output.rstrip()
print(output)
with open('output.txt', 'w') as file:
    file.write(output)