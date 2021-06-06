with open('rosalind_ba9g.txt') as file:
    text = file.readline().rstrip()


def get_suffix_array(text):
    text_len = len(text)
    suffix_list = [(text[i: text_len], i) for i in range(text_len)]
    suffix_array = [i for _, i in sorted(suffix_list)]
    return suffix_array



suffix_array = get_suffix_array(text)
output = ', '.join(map(lambda x: str(x), suffix_array))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)