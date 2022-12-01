def getCoordinates(lines):
    temp = []
    retVal = []
    for line in lines:
        temp.append(line.split(" -> "))
    for tempList in temp:
        for item in tempList:
            retVal.append(item.split(","))

    return retVal


def getMaxCoord(coordinates):
    maxVal = 0
    for coordinate in coordinates:
        for val in coordinate:
            if int(val) > maxVal:
                maxVal = int(val)

    return maxVal
