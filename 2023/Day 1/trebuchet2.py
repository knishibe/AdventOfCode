lines = [line for line in open("input.txt", "r").read().splitlines() if line]

calibration_sum = 0

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(len(lines)):
    line = lines[i]
    firstDigit = 0
    lastDigit = 0
    firstIndex = 1000000
    lastIndex = 0
    firstLoop = True
    for j in range(len(numbers)):
        index = line.find(numbers[j])
        if index != -1:
            l_index = line.rindex(numbers[j])
            if firstLoop:
                firstDigit = j
                lastDigit = j
                firstIndex = index
                lastIndex = l_index
                firstLoop = False
            else:
                if index < firstIndex:
                    firstIndex = index
                    firstDigit = j
                if l_index > lastIndex:
                    lastIndex = l_index
                    lastDigit = j
    for j in range(len(digits)):
        index = line.find(digits[j])
        if index != -1:
            l_index = line.rindex(digits[j])
            if firstLoop:
                firstDigit = j
                lastDigit = j
                firstIndex = index
                lastIndex = l_index
                firstLoop = False
            else:
                if index < firstIndex:
                    firstIndex = index
                    firstDigit = j
                if l_index > lastIndex:
                    lastIndex = l_index
                    lastDigit = j
    calibration_sum += int(str(firstDigit) + str(lastDigit))

print("Calibration Sum: " + str(calibration_sum))

