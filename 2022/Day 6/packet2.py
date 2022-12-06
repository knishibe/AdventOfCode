input = open("input.txt", "r").read().splitlines()

stream = list(input[0])

retVal = 0
for i in range(len(stream)-14):
    packet = stream[i:i+14]
    packetSet = set(packet)
    if len(packet) == len(packetSet):
        retVal = i+14
        break

print("Num Chars: " + str(retVal))
