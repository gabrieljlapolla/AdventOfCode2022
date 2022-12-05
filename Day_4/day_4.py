# Advent of Code 2022 - Day 3

lines = []

# Read in all lines and remove whitespace
with open('day_4_input.txt', 'r') as input:
    lines = [game.strip() for game in input.readlines()] 

test = [
        "3-35,2-4"]
#lines = test

count = 0
for line in lines:
    # Isolate section numbers
    pairs = line.split(',')
    s1, s2 = [int(x) for x in pairs[0].split('-')]
    s3, s4 = [int(x) for x in pairs[1].split('-')]

    # Check if one range is contained within the other
    if ((s1 >= s3 and s2 <= s4)  # First pair contained in second
        or (s3 >= s1 and s4 <= s2) # Second pair contained in first
        and not (s1 == s3 and s2 == s4)): # Ensure pairs are not equal
            count += 1

print(f"Total contained pairs: {count}")
