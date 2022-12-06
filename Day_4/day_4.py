# Advent of Code 2022 - Day 3

lines = []

# Read in all lines and remove whitespace
with open('day_4_input.txt', 'r') as input:
    lines = [game.strip() for game in input.readlines()] 

count = 0
overlaps = 0
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
    
    # Check if pairs overlap
    if (s1 >= s3 and s1 <= s4) or (s3 >=s1 and s3 <= s2):
        overlaps += 1

print(f"Total contained pairs: {count}")
print(f"Overlaps: {overlaps}")
