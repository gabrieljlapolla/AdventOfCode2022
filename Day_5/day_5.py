# Advent of Code 2022 - Day 5

lines = []

# Read in all lines and remove whitespace
with open('day_5_input.txt', 'r') as input:
    lines = input.readlines()

crates = [['T', 'F', 'V', 'Z', 'C', 'W', 'S', 'Q'], 
        ['B', 'R', 'Q'], 
        ['S', 'M', 'P', 'Q', 'T', 'Z', 'B'], 
        ['H', 'Q', 'R', 'F', 'V', 'D'], 
        ['P', 'T', 'S', 'B', 'D', 'L', 'G', 'J'], 
        ['Z', 'T', 'R', 'W'], 
        ['J', 'R', 'F', 'S', 'N', 'M', 'Q', 'H'], 
        ['W', 'H', 'F', 'N', 'R'], 
        ['B', 'R', 'P', 'Q', 'T', 'Z', 'J']]

index = 0
while 'move' not in lines[index]:
    index += 1
instructions = lines[index:] # List of just instructions

# Interpret commands and rearrange lists
for cmd in instructions:
    # Get command
    cmd = cmd.split()
    amt_to_move = int(cmd[1])
    loc_1 = int(cmd[3]) - 1
    loc_2 = int(cmd[-1]) - 1
    # Move crates in list one at a time
    for i in range(0, amt_to_move):
        crates[loc_2].insert(0, crates[loc_1].pop(0))

# Get top crates
top_crates = [crate[0] for crate in crates] 
print(f'Top Crates: {top_crates}')

# -- Part Two --
crates = [['T', 'F', 'V', 'Z', 'C', 'W', 'S', 'Q'], 
        ['B', 'R', 'Q'], 
        ['S', 'M', 'P', 'Q', 'T', 'Z', 'B'], 
        ['H', 'Q', 'R', 'F', 'V', 'D'], 
        ['P', 'T', 'S', 'B', 'D', 'L', 'G', 'J'], 
        ['Z', 'T', 'R', 'W'], 
        ['J', 'R', 'F', 'S', 'N', 'M', 'Q', 'H'], 
        ['W', 'H', 'F', 'N', 'R'], 
        ['B', 'R', 'P', 'Q', 'T', 'Z', 'J']]

# Interpret commands and rearrange lists
for cmd in instructions:
    # Get command
    cmd = cmd.split()
    amt_to_move = int(cmd[1])
    loc_1 = int(cmd[3]) - 1
    loc_2 = int(cmd[-1]) - 1
    # Move crates in list
    crates[loc_2] = crates[loc_1][0:amt_to_move] + crates[loc_2]
    crates[loc_1] = crates[loc_1][amt_to_move:]
    
# Get top crates
top_crates_2 = [crate[0] for crate in crates] 
print(f'Top Crates: {top_crates_2}')