amino_acid_weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                     'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def get_peptide_mass(peptide):
    peptide_sum = 0
    for amino_acid in peptide:
        peptide_sum += amino_acid_weight[amino_acid]
    return peptide_sum


with open('rosalind_ba4c.txt') as file:
    peptide = file.readline().rstrip()

peptide_len = len(peptide)
theoreticalSpectrum = [0]
for currentLen in range(1, peptide_len + 1):
    for i in range(peptide_len):
        endIndex = i + currentLen
        remaining = 0
        if endIndex > peptide_len:
            remaining = endIndex - peptide_len
        currentPeptide = peptide[i:endIndex] + peptide[0:remaining]
        theoreticalSpectrum.append(get_peptide_mass(currentPeptide))
        if currentLen == peptide_len:
            break

theoreticalSpectrum = sorted(theoreticalSpectrum)
output = ' '.join([str(mass) for mass in theoreticalSpectrum])
print(output)
with open('output.txt', 'w') as file:
    file.write(output)










