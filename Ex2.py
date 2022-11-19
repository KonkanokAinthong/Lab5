class BinaryTree:
    root = None

    def Add(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.Add(data)

    def Delete(self, data):
        if self.root != None:
            self.root = self.root.Delete(data)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Add(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.Add(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.Add(data)

    def Delete(self, data):
        if self.data == data:
            if self.left == None and self.right == None:
                return None
            elif self.left != None and self.right == None:
                return self.left
            elif self.left == None and self.right != None:
                return self.right
            else:
                self.data = self.right.GetMin()
                self.right = self.right.Delete(self.data)
        elif data < self.data:
            self.left = self.left.Delete(data)
        else:
            self.right = self.right.Delete(data)
        return self

    def GetMin(self):
        if self.left == None:
            return self.data
        else:
            return self.left.GetMin()

    def Print(self, level=0):
        print("-"*level+str(self.data))
        if self.left != None:
            self.left.Print(level=level + 1)
        if self.right != None:
            self.right.Print(level=level + 1)

    def MaxHeight(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left != None and self.right == None:
            return self.left.MaxHeight() + 1
        elif self.left == None and self.right != None:
            return self.right.MaxHeight() + 1
        else:
            return max(self.left.MaxHeight(), self.right.MaxHeight()) + 1

    def NumberOfParent(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left != None and self.right == None:
            return self.left.NumberOfParent() + 1
        elif self.left == None and self.right != None:
            return self.right.NumberOfParent() + 1
        else:
            return self.left.NumberOfParent() + self.right.NumberOfParent() + 1

    def NumberOfChildren(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left != None and self.right == None:
            return self.left.NumberOfChildren() + 1
        elif self.left == None and self.right != None:
            return self.right.NumberOfChildren() + 1
        else:
            return self.left.NumberOfChildren() + self.right.NumberOfChildren() + 2

    def NumberOfLeaf(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left != None and self.right == None:
            return self.left.NumberOfLeaf()
        elif self.left == None and self.right != None:
            return self.right.NumberOfLeaf()
        else:
            return self.left.NumberOfLeaf() + self.right.NumberOfLeaf()

    def NumberOfSibling(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left != None and self.right == None:
            return self.left.NumberOfSibling()
        elif self.left == None and self.right != None:
            return self.right.NumberOfSibling()
        else:
            return self.left.NumberOfSibling() + self.right.NumberOfSibling() + 1


print("=== Ex2.1 ===")
tree = BinaryTree()
data = [50, 25, 75, 30, 60, 40, 35, 70, 90, 15, 45, 27, 55, 85, 100]
for val in data:
    tree.Add(val)
print("Binary Tree:")
tree.root.Print()
print()

print("=== Ex2.2 ===")
tree.root.Delete(30)
tree.root.Delete(75)
tree.root.Delete(35)
print("Binary Tree:")
tree.root.Print()
print()


print("=== Ex2.3 ===")
print("Max Height:", tree.root.MaxHeight())
print("Number of Parent:", tree.root.NumberOfParent())
print("Number of Children:", tree.root.NumberOfChildren())
print("Number of Leaf:", tree.root.NumberOfLeaf())
print("Number of Sibling:", tree.root.NumberOfSibling())