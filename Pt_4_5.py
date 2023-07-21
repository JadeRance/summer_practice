def find_path(slovar, end, start, path):
    for key, value in slovar.items():
        if end == start:
            print(path[::-1])
            break
        elif end in value:
            if find_path(slovar, key, start, path+key) == None:
                continue
                
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
path = end
candidates = []
find_path(graph, end, start, path)