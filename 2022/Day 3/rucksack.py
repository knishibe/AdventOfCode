lines = [line for line in open("input.txt", "r").read().splitlines() if line]

prioritySum = 0

for i in range(len(lines)):
    items = list(lines[i])
    compartment1 = items[:len(items)//2]
    compartment2 = items[len(items)//2:]
    commonItem = list(set(compartment1).intersection(compartment2))
    priority = ord(commonItem[0])
    if priority > 96:
        prioritySum += priority - 96
    else:
        prioritySum += priority - 38

print("Priority Sum: " + str(prioritySum))