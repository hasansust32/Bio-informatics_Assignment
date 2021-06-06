from collections import Counter


amino_acid_weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                     'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def get_peptide_mass(peptide):
    peptide_sum = 0
    for amino_acid in peptide:
        peptide_sum += amino_acid_weight[amino_acid]
    return peptide_sum


with open('rosalind_ba4f.txt') as file:
    peptide = file.readline().rstrip()
    experimental_spectrum = file.readline().rstrip().split(' ')
    experimental_spectrum = [int(mass) for mass in experimental_spectrum]


def get_score(peptide, experimental_spectrum):
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
    experimental_spectrum_counter = Counter(experimental_spectrum)
    theoretical_spectrum_counter = Counter(theoreticalSpectrum)
    score = 0
    for item in experimental_spectrum_counter:
        current_count = theoretical_spectrum_counter.get(item)
        if current_count is not None:
            score += min(current_count, experimental_spectrum_counter.get(item))
    return score


score = get_score(peptide, experimental_spectrum)
print(score)
with open('output.txt', 'w') as file:
    file.write(str(score))
