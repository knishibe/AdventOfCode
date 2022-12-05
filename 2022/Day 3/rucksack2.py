lines = [line for line in open("input.txt", "r").read().splitlines() if line]

prioritySum = 0

for i in range(0, len(lines)-2, 3):
    elf1 = list(lines[i])
    elf2 = list(lines[i+1])
    elf3 = list(lines[i+2])
    commonItem = list(set(elf1).intersection(elf2, elf3))
    priority = ord(commonItem[0])
    if priority > 96:
        prioritySum += priority - 96
    else:
        prioritySum += priority - 38

print("Priority Sum: " + str(prioritySum))