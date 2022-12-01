import helper
lines = [line for line in open("input.txt", "r").read().splitlines()]
print(lines)

coordinates = helper.getCoordinates(lines)
maxCoord = helper.getMaxCoord(coordinates)
seaMap = [[0 for i in maxCoord] for j in maxCoord]

for i in range(0, int(len(coordinates)/2), 2):

    helper.updateMap(seaMap, coordinates[i], coordinates[i+1])
