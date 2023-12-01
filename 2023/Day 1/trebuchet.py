lines = [line for line in open("input.txt", "r").read().splitlines() if line]

calibration_sum = 0

for i in range(len(lines)):
    line = lines[i]
    firstDigit = 0
    lastDigit = 0
    firstLoop = True
    for j in range(len(line)):
        if line[j].isdigit():
            if firstLoop:
                firstDigit = line[j]
                firstLoop = False
            lastDigit = line[j]
    calibration_sum += int(firstDigit + lastDigit)

print("Calibration Sum: " + str(calibration_sum))

