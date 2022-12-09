def move(direction):
    # if starting beside each other
    if head[1] == tail[1] or head[0] == tail[0]:
        head[0] = head[0] + direction[0]
        head[1] = head[1] + direction[1]
        if head[0] - tail[0] == 2:
            tail[0] += 1
        elif head[0] - tail[0] == -2:
            tail[0] -= 1
        elif head[1] - tail[1] == 2:
            tail[1] += 1
        elif head[1] - tail[1] == -2:
            tail[1] -= 1
    # if starting on the diagonal
    elif head[0] != tail[0] and head[1] != tail[1]:
        head[0] += direction[0]
        head[1] += direction[1]
        if (head[0] - tail[0] == 2 and head[1] - tail[1] == 1) or (head[0] - tail[0] == 1 and head[1] - tail[1] == 2):
            tail[0] += 1
            tail[1] += 1
        elif (head[0] - tail[0] == -2 and head[1] - tail[1] == 1) or (head[0] - tail[0] == -1 and head[1] - tail[1] == 2):
            tail[0] -= 1
            tail[1] += 1
        elif (head[0] - tail[0] == 2 and head[1] - tail[1] == -1) or (head[0] - tail[0] == 1 and head[1] - tail[1] == -2):
            tail[0] += 1
            tail[1] -= 1
        elif (head[0] - tail[0] == -2 and head[1] - tail[1] == -1) or (head[0] - tail[0] == -1 and head[1] - tail[1] == -2):
            tail[0] -= 1
            tail[1] -= 1
    if not any(location == tail for location in tailLocations):
        tailLocations.append(list(tail))


lines = [line for line in open("input.txt", "r").read().splitlines() if line]

head = [0, 0]
tail = [0, 0]
tailLocations = [[0, 0]]

for i in range(len(lines)):
    command = lines[i].split(" ")
    for j in range(int(command[1])):
        if command[0] == "R":
            move([1, 0])
        elif command[0] == "L":
            move([-1, 0])
        elif command[0] == "U":
            move([0, -1])
        elif command[0] == "D":
            move([0, 1])

print("Number of Locations: " + str(len(tailLocations)))