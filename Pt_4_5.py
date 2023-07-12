def find_ways(graph, start, end, way):
    ways = []
    way = way + [start]

    if start == end:
        return [way]

    if not graph.get(start):
        return []

    for neighbor in graph[start]:
        new_ways = find_ways(graph, neighbor, end, way)
        ways.extend(new_ways)

    return ways

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_ways(graph, start, end, path)
print(*paths)
