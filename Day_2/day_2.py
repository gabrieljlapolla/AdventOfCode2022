# Advent of Code 2022 - Day 2

# --- Part One ---
# A, X = Rock       1 Point
# B, Y = Paper      2 Points
# C, Z = Scissors   3 Points
# 6 points for winning, 3 for a draw, 0 for losing

# --- Part Two ---
# X Lose, Y Draw, Z Win

file_name = 'day_2_input.txt'
input = open(file_name, 'r') # Open file
lines = input.readlines() # Read in all lines
lines = [game.strip() for game in lines] # Remove whitespace

# Dicts with solutions to possible combinations
scores  = { 'A X': 3 + 1,      'A Y': 6 + 2,    'A Z': 0 + 3,
            'B X': 0 + 1,      'B Y': 3 + 2,    'B Z': 6 + 3,
            'C X': 6 + 1,      'C Y': 0 + 2,    'C Z': 3 + 3}

scores_two = {  'A X': 0 + 3,      'A Y': 3 + 1,    'A Z': 6 + 2,
                'B X': 0 + 1,      'B Y': 3 + 2,    'B Z': 6 + 3,
                'C X': 0 + 2,      'C Y': 3 + 3,    'C Z': 6 + 1}

score, score_two = 0, 0

# Add up values from scores for each game
for game in lines:
    score += scores[game]
    score_two += scores_two[game]

print(f'Score:      {score}')
print(f'Score Two:  {score_two}')