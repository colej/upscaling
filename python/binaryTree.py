class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

# Allows us to traverse the tree according to the logical
# sequential order.
# This goes to the deepest point first and then pulls
# up to search other branches of the tree.
# This will be important later for algorithms
# that search the tree in a depth-first manner.
def inOrderPrint(node):
    if node is None:
        return
    else:
        inOrderPrint(node.left)
        print(node.data, end = ' ')
        inOrderPrint(node.right)

# Allow
def preOrderPrint(node):
    if node is None:
        return
    else:
        print(node.data, end = ' ')
        preOrderPrint(node.left)
        preOrderPrint(node.right)


def postOrderPrint(node):
    if node is None:
        return
    else:
        print(node.data, end = ' ')
        postOrderPrint(node.right)
        postOrderPrint(node.left)


if __name__ == '__main__':

    root = Node('g') # declare the root of our tree
    # now, add a bunch of cases
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

    inOrderPrint(root)
    print()

    preOrderPrint(root)
    print()

    postOrderPrint(root)
    print()


