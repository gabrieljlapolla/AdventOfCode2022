# Advent of Code 2022 - Day 8

with open('day_8_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

trees = [l.strip() for l in lines] # Remove whitespace

trees2 = ['30373', 
         '25512', 
         '65332', 
         '33549', 
         '35390']


num_visible = 0

for i in range(0, len(trees)):
    for j in range(0, len(trees[0])):
        # If tree is on border it is visible
        if (i == 0 or i == len(trees) - 1
            or j == 0 or j == len(trees[0]) - 1):
            num_visible += 1
        else: # Not on border
            cur_tree = trees[i][j]
            # If any row of trees left, right, above, or below are shorter - tree is visible
            # Check if trees to left and right are bigger
            if all(tree < cur_tree for tree in trees[i][0:j]): # Left
                num_visible += 1
            elif all(tree < cur_tree for tree in trees[i][j + 1:]): # Right
                num_visible += 1
            else: # Check if trees above and below are bigger
                # Get list with column of trees
                col = [row[j] for row in trees]
                if all(tree < cur_tree for tree in col[0:i]): # Above
                    num_visible += 1
                elif all(tree < cur_tree for tree in col[i + 1:]): # Below
                    num_visible += 1

print(f"Number of visible trees: {num_visible}")

# --- Part Two ---
max_scenic_score = 0

for i in range(0, len(trees)):
    for j in range(0, len(trees[0])):
        scenic_score = 0
        tmp_score = 0
        cur_tree = trees[i][j]
        # Count trees to the left
        for t in range(j - 1, -1, -1):
            if trees[i][t] < cur_tree:
                tmp_score += 1
            else:
                tmp_score += 1
                break
        scenic_score = tmp_score
        tmp_score = 0

        # Count trees to the right
        for t in range(j + 1, len(trees[0])):
            if trees[i][t] < cur_tree:
                tmp_score += 1
            else:
                tmp_score += 1
                break
        scenic_score *= tmp_score
        tmp_score = 0

        # Get list with column of trees
        col = [row[j] for row in trees]

        # Count trees above
        for t in range(i - 1, -1, -1):
            if col[t] < cur_tree:
                tmp_score += 1
            else:
                tmp_score += 1
                break

        scenic_score *= tmp_score
        tmp_score = 0
        
        # Count trees below
        for t in range(i + 1, len(trees[0])):
            if col[t] < cur_tree:
                tmp_score += 1
            else:
                tmp_score += 1
                break

        scenic_score *= tmp_score

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(f"Max scenic score: {max_scenic_score}")
