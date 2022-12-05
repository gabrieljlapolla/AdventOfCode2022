# Advent of Code 2022 - Day 3

file_name = 'day_3_input.txt'
input = open(file_name, 'r') # Open file
lines = input.readlines() # Read in all lines
lines = [game.strip() for game in lines] # Remove whitespace

test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']
#lines = test

sum = 0
for line in lines:
    length = int(len(line) / 2) # Length of line
    first_half = line[0:length] # Get halves of line
    last_half = line[length:]
    for char in first_half: # Check chars in first half
        if char in last_half: # Compare chars to last half
            if char.islower():
                sum += ord(char) - 96
            else:
                sum += ord(char) - 38
            break # Match is found so don't check more

print(f'Sum: {sum}')
