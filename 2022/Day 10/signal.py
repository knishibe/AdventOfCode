def check_cycle():
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        return cycle * x
    else:
        return 0


lines = [line for line in open("input.txt", "r").read().splitlines() if line]

x = 1
signal_sum = 0
cycle = 1

for i in range(len(lines)):
    command = lines[i].split(" ")
    if command[0] == "addx":
        signal_sum += check_cycle()
        cycle += 1
        signal_sum += check_cycle()
        x += int(command[1])
        cycle += 1
    else:
        signal_sum += check_cycle()
        cycle += 1

print("Signal Sum: " + str(signal_sum))
