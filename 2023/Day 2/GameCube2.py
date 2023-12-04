import re
lines = [line for line in open("input.txt", "r").read().splitlines() if line]

sum = 0

for i in range(len(lines)):
    line = re.sub('Game \\d: ', '', lines[i])
    line = re.sub(';', ',', line)
    red = 0
    green = 0
    blue = 0
    matches = re.findall('(\\d+) (\\w+)', line)
    for k in range(len(matches)):
        num = matches[k][0]
        col = matches[k][1]
        if str(col) == "red" and int(num) > int(red):
            red = num
        elif str(col) == "green" and int(num) > int(green):
            green = num
        elif str(col) == "blue" and int(num) > int(blue):
            blue = num
    sum += int(red) * int(blue) * int(green)

print("Game Sum: " + str(sum))
