with open('rosalind_ba9h.txt') as file:
    text = file.readline().rstrip()
    pattern_list = [pattern.rstrip() for pattern in file.readlines()]

text += '$'


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


def build_trie(pattern_list):
    root = Node()
    for i, pattern in enumerate(pattern_list):
        current_node = root
        for symbol in pattern:
            child_node = current_node.get_children(symbol)
            if child_node is None:
                child_node = Node(symbol)
                if symbol == '$':
                    child_node.pos = i
                current_node.add_children(child_node)
            current_node = child_node
    return root


def get_match_positions(node):
    match_list = []
    node_queue = [node]
    while len(node_queue) != 0:
        current_node = node_queue.pop(0)
        if current_node.val == '$':
            match_list.append(current_node.pos)
        for child in current_node.children_list:
            node_queue.append(child)
    return match_list



suffix_list = []
for i in range(len(text)):
    suffix_list.append(text[i:len(text)])

suffix_trie_root = build_trie(suffix_list)
match_list = []
for pattern in pattern_list:
    current_node = suffix_trie_root
    pattern_found = True
    for symbol in pattern:
        current_node = current_node.get_children(symbol)
        if current_node is None:
            pattern_found = False
            break
    if pattern_found:
        match_list.extend(get_match_positions(current_node))

output = ' '.join(map(lambda x: str(x), sorted(match_list)))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
