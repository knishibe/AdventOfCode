def check_left(i, j, array, height):
    if j < 0:
        return True
    elif int(array[i][j]) >= height:
        return False
    else:
        return check_left(i, j-1, array, height)


def check_right(i, j, array, height):
    if j >= len(array[i]):
        return True
    elif int(array[i][j]) >= height:
        return False
    else:
        return check_right(i, j+1, array, height)


def check_up(i, j, array, height):
    if i < 0:
        return True
    elif int(array[i][j]) >= height:
        return False
    else:
        return check_up(i-1, j, array, height)


def check_down(i, j, array, height):
    if i >= len(array):
        return True
    elif int(array[i][j]) >= height:
        return False
    else:
        return check_down(i+1, j, array, height)


lines = [line for line in open("input.txt", "r").read().splitlines() if line]
trees = [list(line) for line in lines]

numTrees = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):
        if check_right(int(i), int(j)+1, trees, int(trees[i][j])):
            numTrees += 1
        elif check_left(int(i), int(j)-1, trees, int(trees[i][j])):
            numTrees += 1
        elif check_up(int(i)-1, int(j), trees, int(trees[i][j])):
            numTrees += 1
        elif check_down(int(i)+1, int(j), trees, int(trees[i][j])):
            numTrees += 1

numTrees += len(trees)*2
numTrees += (len(trees[0]) - 2)*2
print("Num Trees: " + str(numTrees))

