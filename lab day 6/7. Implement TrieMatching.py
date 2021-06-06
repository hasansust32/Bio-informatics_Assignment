with open('rosalind_ba9b.txt') as file:
    text = file.readline().rstrip()
    pattern_list = [pattern.rstrip() for pattern in file.readlines()]


class Node:
    def __init__(self, val=None):
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


def prefix_trie_construction(pattern_list):
    root = Node()
    for pattern in pattern_list:
        current_node = root
        for symbol in pattern:
            child_node = current_node.get_children(symbol)
            if child_node is None:
                child_node = Node(symbol)
                current_node.add_children(child_node)
            current_node = child_node
    return root


def prefix_trie_matching(text, node):
    for symbol in text:
        if len(node.children_list) == 0:
            return True
        child_node = node.get_children(symbol)
        if child_node is None:
            return False
        node = child_node
    if len(node.children_list) == 0:
        return True
    return False


prefix_trie_root = prefix_trie_construction(pattern_list)
text_len = len(text)
match_list = []
for i in range(len(text)):
    if prefix_trie_matching(text[i:text_len], prefix_trie_root):
        match_list.append(i)

output = ' '.join(map(lambda x: str(x), match_list))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)


