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

row_len = len(map[0])

# Find start and end locations
for i in range(0, len(map)):
    for j in range(0, row_len):
        loc = f'{i}, {j}'
        graph[loc] = []
        cur_num = ord(map[i][j]) # Current height as int

        if map[i][j] == 'S': # Start position
            start = loc
            cur_num = ord('a') - 1
            map[i][j] = chr(cur_num)
        if map[i][j] == 'E': # End position
            end = loc
            cur_num = ord('z') + 1
            map[i][j] = chr(cur_num)

for i in range(0, len(map)):
    for j in range(0, row_len):
        loc = f'{i}, {j}'
        graph[loc] = []
        cur_num = ord(map[i][j]) # Current height as int

        # Check left
        if (j > 0) and (ord(map[i][j - 1]) - cur_num <= 1):
            graph[loc].append(f'{i}, {j - 1}')
        # Check right
        if (j < (row_len - 1)) and (ord(map[i][j + 1]) - cur_num <= 1):
            graph[loc].append(f'{i}, {j + 1}')
        # Check above
        if (i > 0) and (ord(map[i - 1][j]) - cur_num <= 1):
            graph[loc].append(f'{i - 1}, {j}')
        # Check below
        if (i < (len(map) - 1)) and (ord(map[i + 1][j]) - cur_num <= 1):
            graph[loc].append(f'{i + 1}, {j}')

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

distances = BFS(start)

# Print map of accessible locations
for i in range(0, len(map)):
    print()
    for j in range(0, row_len):
        loc = f'{i}, {j}'
        if loc in distances.keys():
            print(map[i][j], end='')
        else:
            print('.', end='')

print('\n')
print(f"Shortest distance to end: {distances[end]}")