def depth_first_search(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, end, visited):
                return True
    return False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(depth_first_search(graph, 'A', 'F'))  # Output: True
print(depth_first_search(graph, 'B', 'C'))  # Output: False

