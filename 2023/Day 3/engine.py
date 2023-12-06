def is_symbol(character):
    if character != "." and not(str(character).isalpha()) and not(str(character).isnumeric()):
        return True
    else:
        return False


def is_adjacent(row, col, array):
    bool_array = [False, False, False, False, False, False, False, False]

    # same row
    if col - 1 >= 0:
        bool_array[0] = is_symbol(array[row][col - 1])
    if col + 1 < len(array[0]):
        bool_array[1] = is_symbol(array[row][col + 1])

    # row above
    if row - 1 >= 0:
        bool_array[2] = is_symbol(array[row - 1][col])
        if col - 1 >= 0:
            bool_array[3] = is_symbol(array[row - 1][col - 1])
        if col + 1 < len(array[row]):
            bool_array[4] = is_symbol(array[row - 1][col + 1])
    # row below
    if row + 1 < len(array):
        bool_array[5] = is_symbol(array[row + 1][col])
        if col - 1 >= 0:
            bool_array[6] = is_symbol(array[row + 1][col - 1])
        if col + 1 < len(array[row]):
            bool_array[7] = is_symbol(array[row + 1][col + 1])

    return any(bool_array)


lines = [line for line in open("input.txt", "r").read().splitlines() if line]
schematic = [list(line) for line in lines]
sum = 0
for i in range(0, len(schematic)):
    num = ''
    isPart = False
    for j in range(0, len(schematic[i])):
        character = schematic[i][j]
        if str(character).isnumeric():
            num += str(character)
            if not isPart:
                isPart = is_adjacent(i, j, schematic)
        else:
            if isPart:
                sum += int(num)
            num = ''
            isPart = False
    if isPart:
        sum += int(num)
        num = ''
        isPart = False


print("Engine Sum: " + str(sum))



