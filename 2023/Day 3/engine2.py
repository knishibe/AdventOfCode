def get_num(row, col, array):
    num = array[row][col]
    j = col - 1
    while j >= 0:
        digit = array[row][j]
        if str(digit).isnumeric():
            num = digit + num
        else:
            break
        j -= 1
    j = col + 1
    while j < len(array[row]):
        digit = array[row][j]
        if str(digit).isnumeric():
            num = num + digit
        else:
            break
        j += 1
    return num


def get_gear_ratio(row, col, array):
    int_array = [0, 0, 0, 0, 0, 0, 0, 0]

    # same row
    if col - 1 >= 0 and str(array[row][col - 1]).isnumeric():
        int_array[0] = get_num(row, col - 1, array)
    if col + 1 < len(array[0]) and str(array[row][col + 1]).isnumeric():
        int_array[1] = get_num(row, col + 1, array)

    top_left = False
    top_center = False
    bottom_left = False
    bottom_center = False
    # row above
    if row - 1 >= 0:
        # Top Left
        if col - 1 >= 0 and str(array[row - 1][col - 1]).isnumeric():
            int_array[3] = get_num(row - 1, col - 1, array)
            top_left = True
        # Top Center
        if str(array[row - 1][col]).isnumeric():
            top_center = True
            if not top_left:
                int_array[2] = get_num(row - 1, col, array)
        # Top Right
        if col + 1 < len(array[row]) and str(array[row - 1][col + 1]).isnumeric() and not top_center:
            int_array[4] = get_num(row - 1, col + 1, array)
    # row below
    if row + 1 < len(array):
        # Bottom Left
        if col - 1 >= 0 and str(array[row + 1][col - 1]).isnumeric():
            int_array[6] = get_num(row + 1, col - 1, array)
            bottom_left = True
        # Bottom Center
        if str(array[row + 1][col]).isnumeric():
            bottom_center = True
            if not bottom_left:
                int_array[5] = get_num(row + 1, col, array)
        # Bottom Right
        if col + 1 < len(array[row]) and str(array[row + 1][col + 1]).isnumeric() and not bottom_center:
            int_array[7] = get_num(row + 1, col + 1, array)

    parts = [s for s in int_array if s != 0]
    if len(parts) == 2:
        return int(parts[0]) * int(parts[1])
    else:
        return int(0)


lines = [line for line in open("test.txt", "r").read().splitlines() if line]
schematic = [list(line) for line in lines]
sum = 0
for i in range(0, len(schematic)):
    num = ''
    isPart = False
    for j in range(0, len(schematic[i])):
        character = schematic[i][j]
        if str(character) == "*":
            sum += get_gear_ratio(i, j, schematic)


print("Engine Sum: " + str(sum))



