def get_compositions_from_text(text, k):
    compositions = []
    for i in range(len(text) - k):
        compositions.append(text[i: i + k])
    return compositions


Text = ''
k = 0
with open('rosalind_ba3a.txt') as file:
    k = int(file.readline())
    Text = file.readline()
print('\n'.join(sorted(get_compositions_from_text(Text, k))))