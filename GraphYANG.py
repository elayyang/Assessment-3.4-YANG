


from collections import deque


graph = {
    "Y": ["A", "N"],
    "A": ["Y", "G"],
    "N": ["Y", "G"],
    "G": ["A", "N"]
}



def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()



def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:", end=" ")

    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in sorted(graph[vertex]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)



print("GRAPH - YANG")
print("------------")

bfs(graph, "Y")

dfs(graph, "Y")
print()
