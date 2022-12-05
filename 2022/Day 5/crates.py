import re
lines = [line for line in open("input.txt", "r").read().splitlines() if line]

pairs = 0
j = 0
stacks = []
line = lines[j]
while "move" not in line:
    characters = list(line)
    crates = [characters[i:i+4] for i in range(0, len(line), 4)]
    for i in range(len(crates)):
        box = [crate for crate in crates[i] if crate.isalpha()]
        if len(stacks) <= i:
            stacks.append([])
        if box:
            stacks[i].insert(0, box[0])
    j += 1
    line = lines[j]

for i in range(j, len(lines)):
    instructions =  [int(s) for s in re.findall(r'-?\d+\.?\d*', lines[i])]
    numBoxes = instructions[0]
    for j in range(int(numBoxes)):
        box = stacks[int(instructions[1])-1].pop()
        stacks[int(instructions[2])-1].append(box)

for i in range(len(stacks)):
    print(stacks[i][len(stacks[i])-1])