input = open("input.txt", "r").read().splitlines()

stream = list(input[0])

retVal = 0
for i in range(len(stream)-4):
    packet = stream[i:i+4]
    packetSet = set(packet)
    if len(packet) == len(packetSet):
        retVal = i+4
        break

print("Num Chars: " + str(retVal))
