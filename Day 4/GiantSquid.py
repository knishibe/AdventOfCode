import helper
lines = [line for line in open("input.txt", "r").read().splitlines()]

callNumbers = lines[0].split(",")
lines.pop(0)
lines.pop(0)

bingoSheets = helper.getBingoSheets(lines)

winningBingoSheet = []
winningNum = 0
for num in callNumbers:
    for bingoSheet in bingoSheets:
        helper.playNumber(bingoSheet, num)
        if helper.checkBingoSheet(bingoSheet):
            winningBingoSheet = bingoSheet
            break
    if winningBingoSheet:
        winningNum = num
        break


print(winningNum)
print(winningBingoSheet)
print(helper.getSum(winningBingoSheet)*int(winningNum))


