lines = [line for line in open("input.txt", "r").read().splitlines()]

lanternFish = lines[0].split(",")
lanternFish = [int(fish) for fish in lanternFish]
days = 80
newFish = []
for k in range(days):
    newFish = []
    for i in range(len(lanternFish)):
        if lanternFish[i] == 0:
            newFish.append(8)
            lanternFish[i] = 6
        else:
            lanternFish[i] -= 1
    lanternFish.extend(newFish)

print(len(lanternFish))

