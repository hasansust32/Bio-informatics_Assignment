from Bio.Seq import Seq
text = ''
peptide = ''

with open('rosalind_ba4b.txt') as file:
    text = file.readline().rstrip()
    peptide = file.readline().rstrip()

pattern_list = []
pattern_len = len(peptide) * 3

for i in range(len(text) - pattern_len + 1):
    pattern = Seq(text[i: i+pattern_len]).transcribe()
    reversePattern = pattern.reverse_complement()
    if str(pattern.translate()) == peptide or str(reversePattern.translate()) == peptide:
        pattern_list.append(str(pattern.back_transcribe()))

output = '\n'.join(pattern_list)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)

