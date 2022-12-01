lines = [line for line in open("input.txt", "r").read().splitlines() if line]

oRate = 0
cRate = 0
numBits = len(lines[0])
oOnes = 0
cOnes = 0
oList = lines
cList = lines
cBits = 0
oBits = 0

for i in range(numBits):
    oOnes = 0
    cOnes = 0
    for line in oList:
        if int(line[i]) == 1:
            oOnes += 1
    for line in cList:
        if int(line[i]) == 1:
            cOnes += 1
    if oOnes >= len(oList) / 2:
        oList = [line for line in oList if int(line[i]) == 1]
    else:
        oList = [line for line in oList if int(line[i]) == 0]

    if cOnes >= len(cList) / 2:
        cList = [line for line in cList if int(line[i]) == 0]
    else:
        cList = [line for line in cList if int(line[i]) == 1]

    if len(list(oList)) == 1:
        oBits = oList[0]
    if len(list(cList)) == 1:
        cBits = cList[0]

for i in range(numBits):
    if int(oBits[i]) == 1:
        oRate += 2 ** (numBits-1-i)
    if int(cBits[i]) == 1:
        cRate += 2 ** (numBits-1-i)


print("Oxygen Rate: " + str(oRate))
print("Carbon Dioxide Rate: " + str(cRate))
print("Answer: " + str(oRate*cRate))
