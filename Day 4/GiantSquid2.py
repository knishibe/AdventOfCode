import helper
lines = [line for line in open("input.txt", "r").read().splitlines()]

callNumbers = lines[0].split(",")
lines.pop(0)
lines.pop(0)

bingoSheets = helper.getBingoSheets(lines)

bingoSheetTracker = [0]*len(bingoSheets)
winningNum = 0
winningBingoSheet = []
for num in callNumbers:
    for i in range(len(bingoSheets)):
        bingoSheet = bingoSheets[i]
        helper.playNumber(bingoSheet, num)
        if helper.checkBingoSheet(bingoSheet):
            bingoSheetTracker[i] = 1
        if 0 not in bingoSheetTracker:
            winningNum = num
            winningBingoSheet = bingoSheet
            break
    if winningBingoSheet:
        break


print(winningNum)
print(winningBingoSheet)
print(helper.getSum(winningBingoSheet)*int(winningNum))


