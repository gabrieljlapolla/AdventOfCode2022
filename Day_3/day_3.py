# Advent of Code 2022 - Day 3

file_name = 'day_3_input.txt'
lines = []

with open(file_name, 'r') as input:
    lines = input.readlines() # Read in all lines

lines = [game.strip() for game in lines] # Remove whitespace

sum = 0
for line in lines:
    length = int(len(line) / 2) # Length of line
    first_half = line[0:length] # Get halves of line
    last_half = line[length:]
    for char in first_half: # Check chars in first half
        if char in last_half: # Compare chars to last half
            if char.islower():
                sum += ord(char) - 96 # Convert letter to value
            else:
                sum += ord(char) - 38
            break # Match is found so don't check more

print(f'Sum: {sum}')

# --- Part Two ---
p_sum = 0
for i in range(0, len(lines), 3): # Iterate by grous of 3 lines
    line_1 = lines[i]
    line_2 = lines[i + 1]
    line_3 = lines[i + 2]
    for char in line_1:
        if char in line_2 and char in line_3: # If all three contain the same letter
            if char.islower():
                p_sum += ord(char) - 96 # Convert letter to value
            else:
                p_sum += ord(char) - 38
            break # Match is found so don't check more

print(f'Priorities sum: {p_sum}')
