def check_cycle():
    if 2 >= (cycle % 40) - x >= 0:
        return "#"
    else:
        return "."


lines = [line for line in open("input.txt", "r").read().splitlines() if line]

x = 1
displayLine = ""
cycle = 1

for i in range(len(lines)):
    command = lines[i].split(" ")
    if command[0] == "addx":
        displayLine += check_cycle()
        if cycle % 40 == 0:
            print(displayLine)
            displayLine = ""
        cycle += 1
        displayLine += check_cycle()
        if cycle % 40 == 0:
            print(displayLine)
            displayLine = ""
        x += int(command[1])
        cycle += 1
    else:
        displayLine += check_cycle()
        if cycle % 40 == 0:
            print(displayLine)
            displayLine = ""
        cycle += 1


