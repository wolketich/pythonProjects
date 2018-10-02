# Define the depth first search function
def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

def generate_graph():
    graph = {}
    graph['A'] = set(['B', 'C'])
    graph['B'] = set(['A', 'D', 'E'])
    graph['C'] = set(['A', 'F'])
    graph['D'] = set(['B'])
    graph['E'] = set(['B', 'F'])
    graph['F'] = set(['C', 'E'])
    return graph
