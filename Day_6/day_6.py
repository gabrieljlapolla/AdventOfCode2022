# Advent of Code 2022 - Day 6

line = []

# Read in all line and remove whitespace
with open('day_6_input.txt', 'r') as input:
    line = input.readline().strip() 

i = 0
marker = -1
marker_len = 14

# Iterate over line checking the next marker_len characters
while i < len(line) - marker_len:
    # Use a dict to store values
    chars = {}
    for j in range(0, marker_len):
        chars[line[j + i]] = j + i
    # If the dictionary length is the marker_len, no values repeat
    if len(chars) == marker_len:
        marker = i + marker_len
        break
    i += 1

print(f'Marker: {marker}')