
from collections import deque



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node("Y")
root.left = Node("A")
root.right = Node("N")
root.left.left = Node("G")



def bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()



def dfs(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs(root.left)
    dfs(root.right)



print("BINARY TREE - YANG")
print("------------------")

bfs(root)

print("DFS Traversal:", end=" ")
dfs(root)
print()
