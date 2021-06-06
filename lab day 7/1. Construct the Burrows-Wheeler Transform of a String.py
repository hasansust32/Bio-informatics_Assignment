with open('rosalind_ba9i.txt') as file:
    text = file.readline().rstrip()
 
bw_mat = []
for i in range(len(text)):
    bw_mat.append(text[i: len(text)] + text[0: i])
bwt = ''.join([pattern[-1] for pattern in sorted(bw_mat)])
print(bwt)
with open('output.txt', 'w') as file:
    file.write(bwt)