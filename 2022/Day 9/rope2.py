def move(head, tail, direction, is_tail, is_head):
    if is_head:
        head[0] = head[0] + direction[0]
        head[1] = head[1] + direction[1]
    # if starting beside each other
    v_diff = head[1]-tail[1]
    h_diff = head[0]-tail[0]
    # if starting beside each other
    if (head[1] == tail[1] or head[0] == tail[0]) and (abs(v_diff) == 2 or abs(h_diff) == 2):
        if h_diff == 2:
            tail[0] += 1
        elif h_diff == -2:
            tail[0] -= 1
        elif v_diff == 2:
            tail[1] += 1
        elif v_diff == -2:
            tail[1] -= 1
    # if starting on the diagonal
    elif head[0] != tail[0] and head[1] != tail[1]:
        if (h_diff >= 2 and v_diff >= 1) or (h_diff >= 1 and v_diff >= 2):
            tail[0] += 1
            tail[1] += 1
        elif (h_diff <= -2 and v_diff >= 1) or (h_diff <= -1 and v_diff >= 2):
            tail[0] -= 1
            tail[1] += 1
        elif (h_diff >= 2 and v_diff <= -1) or (h_diff >= 1 and v_diff <= -2):
            tail[0] += 1
            tail[1] -= 1
        elif (h_diff <= -2 and v_diff <= -1) or (h_diff <= -1 and v_diff <= -2):
            tail[0] -= 1
            tail[1] -= 1
    if is_tail and not any(location == tail for location in tailLocations):
        tailLocations.append(list(tail))


lines = [line for line in open("input.txt", "r").read().splitlines() if line]

knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tailLocations = [[0, 0]]

for i in range(len(lines)):
    command = lines[i].split(" ")
    for j in range(int(command[1])):
        for k in range(len(knots)-1):
            if command[0] == "R":
                move(knots[k], knots[k+1], [1, 0], k+1 == len(knots)-1, k == 0)
            elif command[0] == "L":
                move(knots[k], knots[k+1], [-1, 0], k+1 == len(knots)-1, k == 0)
            elif command[0] == "U":
                move(knots[k], knots[k+1], [0, -1], k+1 == len(knots)-1, k == 0)
            elif command[0] == "D":
                move(knots[k], knots[k+1], [0, 1], k+1 == len(knots)-1, k == 0)

print("Number of Locations: " + str(len(tailLocations)))
