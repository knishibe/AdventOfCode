lines = [line for line in open("input.txt", "r").read().splitlines() if line]

pairs = 0

for i in range(len(lines)):
    assignments = lines[i].split(',')
    elf1 = assignments[0].split('-')
    elf2 = assignments[1].split('-')
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        pairs += 1
    elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        pairs += 1

print("Pairs: " + str(pairs))