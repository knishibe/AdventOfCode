def getBingoSheets(lines):
    bingoSheets = []
    tempArray = []
    for i in range(len(lines)):
        j = 0
        if lines[i] == "":
            j += 1
            bingoSheets.append(tempArray)
            tempArray = []
        tempArray.append(lines[i].split(" "))

    bingoSheets.append(tempArray)

    for i in range(len(bingoSheets)):
        for j in range(len(bingoSheets[i])):
            try:
                while True:
                    bingoSheets[i][j].remove("")
            except ValueError:
                pass

    for i in range(len(bingoSheets)):
        bingoSheets[i] = [line for line in bingoSheets[i] if line]

    return bingoSheets


def playNumber(bingoSheet, num):
    for i in range(len(bingoSheet)):
        for j in range(len(bingoSheet[i])):
            if bingoSheet[i][j] == num:
                bingoSheet[i][j] = "*"


def checkBingoSheet(bingoSheet):
    horizontal = [0]*len(bingoSheet[0])
    for i in range(len(bingoSheet)):
        vertical = 0
        for j in range(len(bingoSheet[i])):
            if bingoSheet[i][j] == "*":
                vertical += 1
                horizontal[j] += 1

        if vertical == len(bingoSheet[i]):
            return True

    for i in range(len(horizontal)):
        if horizontal[i] == len(bingoSheet):
            return True

    return False


def getSum(bingoSheet):
    bingoSum = 0
    for i in range(len(bingoSheet)):
        for j in range(len(bingoSheet[i])):
            if bingoSheet[i][j] != "*":
                bingoSum += int(bingoSheet[i][j])

    return bingoSum
