lines = [line for line in open("input.txt", "r").read().splitlines() if line]

score = 0

for i in range(len(lines)):
    players = lines[i].split(" ")
    player1 = ord(players[0]) - 64
    player2 = ord(players[1]) - 87
    playerDiff = player1 - player2
    if player1 == player2:
        score += 3 + player2
    elif (playerDiff < 0 and playerDiff > -2) or playerDiff == 2:
        score += 6 + player2
    elif (playerDiff > 0 and playerDiff < 2) or playerDiff == -2:
        score += player2

print("Score: " + str(score))