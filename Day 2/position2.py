lines = [line for line in open("input.txt", "r").read().splitlines() if line]
hPos = 0
depth = 0
aim = 0

for i in range(len(lines)):
    line = lines[i].split()
    if line[0].lower() == "forward":
        hPos += int(line[1])
        depth += int(line[1])*aim
    elif line[0].lower() == "up":
        aim -= int(line[1])
    elif line[0].lower() == "down":
        aim += int(line[1])

print("horizontal position: " + str(hPos))
print("depth: " + str(depth))
print("product: " + str(depth*hPos))
