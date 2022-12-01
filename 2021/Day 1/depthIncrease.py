lines = [int(line) for line in open("input.txt", "r").read().splitlines() if line]
numIncreases = 0
numChecks = 0
for i in range(len(lines) - 1):
    numChecks += 1
    if lines[i] < lines[i+1]:
        numIncreases += 1
        print("Increase")
    else:
        print("Decrease")

print("Number of Increases: " + str(numIncreases))
print("Number of Checks: " + str(numChecks))

