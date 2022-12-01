lines = [line for line in open("input.txt", "r").read().splitlines()]

lanternFish = lines[0].split(",")
lanternFish = [int(fish) for fish in lanternFish]
days = 256
totalFish = 0
numLanternFish = [0]*9

for i in range(len(numLanternFish)):
    numLanternFish[i] = lanternFish.count(i)

for k in range(days):
    breeders = numLanternFish.pop(0)
    numLanternFish[6] += breeders
    numLanternFish.append(breeders)

for i in range(len(numLanternFish)):
    totalFish += numLanternFish[i]
print(totalFish)

