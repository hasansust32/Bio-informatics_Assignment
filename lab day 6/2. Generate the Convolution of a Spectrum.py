with open('rosalind_ba4h.txt') as file:
    spectrum = sorted([int(mass) for mass in file.readline().rstrip().split(' ')])


def get_convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(0, i):
            diff = spectrum[i] - spectrum[j]
            if diff != 0:
                convolution.append(diff)
    return convolution




output = ' '.join([str(mass) for mass in sorted(get_convolution(spectrum))])
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
