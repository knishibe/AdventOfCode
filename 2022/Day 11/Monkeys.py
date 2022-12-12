import re
class Monkey:
    def __init__(self, items, operation, test, true_pass, false_pass):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_pass = true_pass
        self.false_pass = false_pass
        self.num_inspections = 0


lines = [line for line in open("input.txt", "r").read().splitlines() if line]
monkeys = []
for i in range(0, len(lines), 6):
    m_items = lines[i+1].replace("  Starting items: ", "").split(", ")
    m_operation = lines[i+2].replace("  Operation: new = old ", "")
    m_test = int(re.findall(r'\d+', lines[i+3])[0])
    m_true_pass = int(re.findall(r'\d+', lines[i+4])[0])
    m_false_pass = int(re.findall(r'\d+', lines[i+5])[0])
    monkeys.append(Monkey(m_items, m_operation, m_test, m_true_pass, m_false_pass))

for i in range(20):
    for j in range(len(monkeys)):
        monkey = monkeys[j]
        while len(monkey.items) > 0:
            worry = int(monkey.items.pop(0))
            monkey.num_inspections += 1
            if monkey.operation == "* old":
                worry = worry * worry
            else:
                worry = eval(str(worry) + monkey.operation)
            worry = int(worry / 3)
            if worry % monkey.test == 0:
                monkeys[monkey.true_pass].items.append(worry)
            else:
                monkeys[monkey.false_pass].items.append(worry)

inspections = [monkey.num_inspections for monkey in monkeys if monkey]
maxInsp = max(inspections)
inspections.remove(maxInsp)
maxInsp2 = max(inspections)
print("Monkey Business: " + str(maxInsp*maxInsp2))
