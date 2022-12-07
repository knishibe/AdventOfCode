class TreeNode:
    def __init__(self, is_dir, parent, name):
        self.is_dir = is_dir
        self.size = 0
        self.parent = parent
        self.name = name
        self.children = []

    def set_size(self, size):
        self.size = size

    def get_size(self):
        size = 0
        if self.is_dir:
            for j in range(len(self.children)):
                size += self.children[j].get_size()
            return size
        else:
            return self.size

    def add_child(self, child):
        self.children.append(child)


def get_size_sum(node):
    if not node.is_dir:
        return 0
    else:
        sum_of_size = 0
        current_size = node.get_size()
        if current_size <= 100000:
            sum_of_size += current_size
        for j in range(len(node.children)):
            sum_of_size += get_size_sum(node.children[j])
        return sum_of_size


lines = [line for line in open("input.txt", "r").read().splitlines() if line]
root = TreeNode(True, None, "/")
sumOfSize = 0
currentNode = None
for i in range(len(lines)):
    command = lines[i].split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                currentNode = root
            elif command[2] == "..":
                currentNode = currentNode.parent
            else:
                matchingChild = [child for child in currentNode.children if child.name == command[2]]
                if len(matchingChild) > 0:
                    currentNode = matchingChild[0]
                else:
                    newChild = TreeNode(True, currentNode, command[2])
                    currentNode.add_child(newChild)
                    currentNode = newChild
    elif command[0] == "dir":
        matchingChild = [child for child in currentNode.children if child.name == command[1]]
        if len(matchingChild) == 0:
            currentNode.add_child(TreeNode(True, currentNode, command[1]))
    else:
        newChild = TreeNode(False, currentNode, command[1])
        newChild.set_size(int(command[0]))
        currentNode.add_child(newChild)

sumOfSize = get_size_sum(root)
print("Size sum: " + str(sumOfSize))
