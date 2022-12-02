lines = [line for line in open("input.txt", "r").read().splitlines() if line]

score = 0

for i in range(len(lines)):
    players = lines[i].split(" ")
    player = ord(players[0]) - 64
    outcome = players[1]

    if outcome == 'X':
        choice = player - 1
        if choice <= 0:
            choice = 3
        score += choice
    elif outcome == 'Y':
        score += 3 + player
    elif outcome == 'Z':
        choice = player + 1
        if choice > 3:
            choice = 1
        score += 6 + choice

print("Score: " + str(score))