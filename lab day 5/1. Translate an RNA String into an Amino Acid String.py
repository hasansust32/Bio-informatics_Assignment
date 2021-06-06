from Bio.Seq import Seq
Pattern = ''

with open('rosalind_ba4a.txt') as file:
    Pattern = file.readline().rstrip()

rna = Seq(Pattern)
protein = rna.translate(to_stop=True)
print(protein)
with open('output.txt', 'w') as file:
    file.write(str(protein))