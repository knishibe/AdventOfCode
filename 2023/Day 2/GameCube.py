import re
lines = [line for line in open("input.txt", "r").read().splitlines() if line]

red = 12
green = 13
blue = 14

sum = 0

for i in range(len(lines)):
    line = re.sub('Game \\d: ', '', lines[i])
    line = re.sub(';', ',', line)
    matches = re.findall('(\\d+) (\\w+)', line)
    possible = True
    for j in range(len(matches)):
        num = matches[j][0]
        col = matches[j][1]
        if str(col) == "red" and int(num) > red:
            possible = False
            break
        elif str(col) == "green" and int(num) > green:
            possible = False
            break
        elif str(col) == "blue" and int(num) > blue:
            possible = False
            break
    if possible:
        sum += i+1

print("Game Sum: " + str(sum))
