lines = [line for line in open("input.txt", "r").read().splitlines() if line]

eRate = 0
gRate = 0
numBits = len(lines[0])
numOnes = [0]*numBits

for i in range(len(lines)):
    for j in range(numBits):
        if int(lines[i][j]) == 1:
            numOnes[j] += 1

for i in range(numBits):
    if numOnes[i] > len(lines) / 2:
        gRate += 2 ** (numBits-1-i)
    else:
        eRate += 2 ** (numBits-1-i)


print("Gamma Rate: " + str(gRate))
print("Epsilon Rate: " + str(eRate))
print("Answer: " + str(eRate*gRate))
