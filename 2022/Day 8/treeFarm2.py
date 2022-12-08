def check_left(i, j, array, height, score):
    if j < 0:
        return score
    elif int(array[i][j]) >= height:
        return score + 1
    else:
        return check_left(i, j-1, array, height, score + 1)


def check_right(i, j, array, height, score):
    if j >= len(array[i]):
        return score
    elif int(array[i][j]) >= height:
        return score + 1
    else:
        return check_right(i, j+1, array, height, score + 1)


def check_up(i, j, array, height, score):
    if i < 0:
        return score
    elif int(array[i][j]) >= height:
        return score + 1
    else:
        return check_up(i-1, j, array, height, score + 1)


def check_down(i, j, array, height, score):
    if i >= len(array):
        return score
    elif int(array[i][j]) >= height:
        return score + 1
    else:
        return check_down(i+1, j, array, height, score + 1)


lines = [line for line in open("input.txt", "r").read().splitlines() if line]
trees = [list(line) for line in lines]

highestScore = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):
        right = check_right(int(i), int(j)+1, trees, int(trees[i][j]), 0)
        left = check_left(int(i), int(j)-1, trees, int(trees[i][j]), 0)
        up = check_up(int(i)-1, int(j), trees, int(trees[i][j]), 0)
        down = check_down(int(i)+1, int(j), trees, int(trees[i][j]), 0)
        totalScore = right * left * up * down
        if totalScore > highestScore:
            highestScore = totalScore

print("Highest Score: " + str(highestScore))

