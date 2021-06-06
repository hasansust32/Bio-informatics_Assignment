from collections import Counter

amino_acid_weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                     'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
acids = list(amino_acid_weight.keys())

with open('rosalind_ba4i.txt') as file:
    conv_limit = int(file.readline().rstrip())
    leaderboard_limit = int(file.readline().rstrip())
    spectrum = sorted([int(mass) for mass in file.readline().rstrip().split(' ')])


def get_convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(0, i):
            diff = spectrum[i] - spectrum[j]
            if diff != 0:
                convolution.append(diff)
    return convolution



def expand_with_score(leaderboard, spectrum):
    current_len = len(leaderboard)
    for i in range(current_len):
        peptide = leaderboard[i][0]
        for acid in acids:
            new_peptide = peptide + acid
            new_score = get_score(new_peptide, spectrum)
            leaderboard.append((new_peptide, new_score))
    del leaderboard[i: current_len]
    return leaderboard


def get_mass(peptide):
    mass = 0
    for acid in peptide:
        mass += amino_acid_weight[acid]
    return mass


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
            theoreticalSpectrum.append(get_mass(currentPeptide))
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


def cut_leaderboard(leaderboard, limit):
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    while limit < len(leaderboard) and leaderboard[limit][1] == leaderboard[limit - 1][1]:
        limit += 1
    leaderboard = leaderboard[:limit]
    return leaderboard


def cut_convolution(convolution, limit):
    conv_counter = Counter(convolution)
    conv_counter = conv_counter.most_common()
    # print(conv_counter)
    while limit < len(conv_counter) and conv_counter[limit][1] == conv_counter[limit - 1][1]:
        limit += 1
    conv_counter = conv_counter[:limit]
    convolution = []
    for mass, count in conv_counter:
        convolution.extend([mass] * count)
    return convolution


def cut_amino_acid(convolution):
    unique_mass = set(convolution)
    delete_key_list = []
    for acid in amino_acid_weight:
        if amino_acid_weight[acid] not in unique_mass:
            delete_key_list.append(acid)
    for key in delete_key_list:
        del amino_acid_weight[key]
        acids.remove(key)
    return amino_acid_weight


def leaderboard_cyclopeptide_sequencing(spectrum, limit):
    leader_peptide = ''
    leader_score = 0
    leaderboard = [(leader_peptide, leader_score)]
    current_try = 0
    while len(leaderboard) != 0:
        leaderboard = expand_with_score(leaderboard, spectrum)
        remove_list = []
        for i in range(len(leaderboard)):
            peptide = leaderboard[i][0]
            score = leaderboard[i][1]
            current_mass = get_mass(peptide)
            if current_mass == spectrum[-1]:
                if score > leader_score:
                    leader_peptide = peptide
                    leader_score = score
            elif current_mass > spectrum[-1]:
                remove_list.append(i)

        for i in remove_list[::-1]:
            del leaderboard[i]

        leaderboard = cut_leaderboard(leaderboard, limit)
        current_try += 1
        print(current_try, leader_peptide, leader_score, len(leaderboard))
        # if current_try == 25:
        #     break
    return leader_peptide


convolution = get_convolution(spectrum)
convolution = sorted([mass for mass in convolution if 57 <= mass <= 200])
convolution = cut_convolution(convolution, conv_limit)
amino_acid_weight = cut_amino_acid(convolution)
leader_peptide = leaderboard_cyclopeptide_sequencing(spectrum, leaderboard_limit)
print(leader_peptide)
masses = list(map(lambda x: amino_acid_weight[x], leader_peptide))
output = '-'.join(list(map(lambda x: str(x), masses)))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)