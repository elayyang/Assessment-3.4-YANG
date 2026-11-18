

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)



def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")



root = Node("E")

root.left = Node("L")
root.right = Node("I")

root.left.left = Node("Z")
root.left.right = Node("A")

root.left.left.left = Node("N")
root.left.left.right = Node("G")

root.right.left = Node("Y")
root.right.right = Node("A")



print("DFS Methods in Binary Tree")

print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()
