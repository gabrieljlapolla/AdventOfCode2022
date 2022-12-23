# Advent of Code 2022 - Day 12

with open('day_12_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

map = [l.strip() for l in lines] # Remove whitespace
map = [list(l) for l in map]

# Build graph out of map so graph algorithm can be used to find shortest path
# Graph contains possible movements from each position
graph = {}
start = ''
end = ''
a_list = []

row_len = len(map[0])

# Find start and end locations
for i in range(0, len(map)):
    for j in range(0, row_len):
        loc = f'{i}, {j}'
        cur_num = ord(map[i][j]) # Current height as int
        if map[i][j] == 'S': # Start position
            start = loc
            cur_num = ord('a')
            map[i][j] = chr(cur_num)
        if map[i][j] == 'E': # End position
            end = loc
            cur_num = ord('z')
            map[i][j] = chr(cur_num)

for i in range(0, len(map)):
    for j in range(0, row_len):
        loc = f'{i}, {j}'
        graph[loc] = []
        cur_num = ord(map[i][j]) # Current height as int

        # Check left
        if (j > 0) and (ord(map[i][j - 1]) - cur_num >= -1):
            graph[loc].append(f'{i}, {j - 1}')
        # Check right
        if (j < (row_len - 1)) and (ord(map[i][j + 1]) - cur_num >= -1):
            graph[loc].append(f'{i}, {j + 1}')
        # Check above
        if (i > 0) and (ord(map[i - 1][j]) - cur_num >= -1):
            graph[loc].append(f'{i - 1}, {j}')
        # Check below
        if (i < (len(map) - 1)) and (ord(map[i + 1][j]) - cur_num >= -1):
            graph[loc].append(f'{i + 1}, {j}')

        # Save all 'a' coordinates for part two
        if map[i][j] == 'a':
            a_list.append(loc)

# Breadth first search on graph
def BFS(start):
    queue = []
    visited = []
    distances = {}
    queue.append(start)
    visited.append(start)
    distances[start] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if not neighbor in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                distances[neighbor] = distances[current] + 1
    return distances

distances = BFS(end)
print(f"Shortest distance to end: {distances[start]}")

# -- Part Two -- 
# To make part two simpler, instead of finding a path start to finish,
# a path was found from finish to start.
# This results in the smallest 'a' value in distances being the answer
min_a = distances[start]
for pos in a_list:
    if pos in distances.keys() and distances[pos] < min_a:
        min_a = distances[pos]

print(f"Shortest distance to end from any elevation a: {min_a}")