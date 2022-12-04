# Advent of Code 2022 - Day 1

file_name = 'day_1_input.txt'
input = open(file_name, 'r') # Open file
lines = input.readlines() # Read in all lines

all_calories = [] # List of sums of each elf's calories
current_calories = 0

for line in lines:
    if line != '\n': # Add calories for a single elf together
        current_calories += int(line.strip())
    else: # New elf
        all_calories.append(current_calories)
        current_calories = 0 # Reset calorie counter

all_calories.sort()
top_3_calories = sum(all_calories[-3:]) # Add top 3 values

print(f'Highest Calories: {all_calories[-1]}')
# Total of top three highest calories
print(f'Top 3 Calories: {top_3_calories}')