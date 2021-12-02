lines = [line for line in open("input.txt", "r").read().splitlines() if line]
hPos = 0
vPos = 0

for i in range(len(lines)):
    line = lines[i].split()
    if line[0].lower() == "forward":
        hPos += int(line[1])
    elif line[0].lower() == "up":
        vPos -= int(line[1])
    elif line[0].lower() == "down":
        vPos += int(line[1])

print("horizontal position: " + str(hPos))
print("vertical position: " + str(vPos))
print("product: " + str(vPos*hPos))
