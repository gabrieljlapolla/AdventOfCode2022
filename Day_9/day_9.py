# Advent of Code 2022 - Day 9

with open('day_9_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

steps = [l.strip() for l in lines] # Remove whitespace

pos_visited = []
nums = 0;
length = 2 # Entire length including head and tail
# Part Two: 
length = 10

# Node contains location of every node in rope
nodes = [[0,0] for n in range(0, length)]

for step in steps:
    dir, num = step.split()
    num = int(num)
    for i in range(0, num):
        if dir == 'R': # Right
            nodes[0][0] += 1
        elif dir == 'L': # Left
            nodes[0][0]  -= 1
        elif dir == 'U': # Up
            nodes[0][1]  += 1
        elif dir == 'D': # Down
            nodes[0][1]  -= 1

        # Update each node individually based on location of previous node
        for n in range(1, length):
            prev_x_cur = nodes[n - 1][0] - nodes[n][0] # Distance between previous node and current
            prev_y_cur = nodes[n - 1][1] - nodes[n][1]

            # Distance between current node and previous node
            distance = (prev_x_cur ** 2 + prev_y_cur ** 2) ** 0.5

            # Check if head is more than one space away
            if (distance > 2):
                nodes[n][0] += int(abs(prev_x_cur) / prev_x_cur)
                nodes[n][1] += int(abs(prev_y_cur) / prev_y_cur)
            else:
                if (abs(prev_x_cur) > 1):
                    nodes[n][0] += int(abs(prev_x_cur) / prev_x_cur)
                if (abs(prev_y_cur) > 1):
                    nodes[n][1] += int(abs(prev_y_cur) / prev_y_cur)

        if not nodes[length - 1] in pos_visited:
            pos_visited.append(nodes[length - 1].copy())

print(f"Positions visited by tail at least once: {len(pos_visited)}")