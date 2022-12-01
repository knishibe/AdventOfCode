lines = [line.split('\n') for line in open("input.txt", "r").read().split('\n\n') if line]
calories = 0
elves = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        calories += int(lines[i][j])
    elves.append(calories)
    calories = 0
elf1 = max(elves)
elves.remove(elf1)
elf2 = max(elves)
elves.remove(elf2)
elf3 = max(elves)
elves.remove(elf3)
print("Biggest Elf Calories: " + str(elf1 + elf2 + elf3))