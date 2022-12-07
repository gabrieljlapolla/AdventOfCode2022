# Advent of Code 2022 - Day 7

with open('Day_7/day_7_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

lines = [game.strip() for game in lines] # Remove whitespace

base_dir = '/'
dir_divider = '-'
dir = [] # Current directory
dirs = {} # Directory as key with contents as list value
for i in range(0, len(lines)):
    cmd = lines[i].split()
    # ls is the only other command so no need to check for it
    # if it is not cd, it is ls
    if cmd[0] == '$': 
        if cmd[1] == 'cd': # Command is cd
            if (cmd[2] == '..'): # Remove a dir
                dir.pop()
            else: # Add dir
                dir.append(cmd[2])
            if dir_divider.join(dir) not in dirs: # Check if dir is saved
                dirs[dir_divider.join(dir)] = [] # Add dir to dict
    else: # If it is not a cmd it is file info from ls
        dirs[dir_divider.join(dir)].append(cmd)

# dirs now contains all the structured info needed to calculate dir size

dir_sizes = {} # Will contain all dirs with their sizes

# Recursive helper function to get size of dir
def get_dir_size(cur_dir):
    size = 0
    # Check all contents dir and sum their sizes
    for entry in dirs[cur_dir]:
        if entry[0] == 'dir': # Is a dir
            if cur_dir not in dir_sizes: # dir size not known
                next_dir = cur_dir + dir_divider + entry[1] # Get whole dir as string
                dir_sizes[next_dir] = get_dir_size(next_dir) # Add size info to dict
                size += dir_sizes[next_dir]
            else:
                size += dir_sizes[cur_dir] # Add size of sub dirs
        else: # Is a file
            size += int(entry[0])
    return size # Size of input directory including all contents and sub-dirs

# Get sizes for all dirs starting from base dir
dir_sizes[base_dir] = get_dir_size(base_dir)
    
# dir_sizes now contains the sizes of all dirs including their sub-dirs
# Iterate over dir_sizes and add up all dirs with a total size of at most 100,000
sum = 0
for dir, size in dir_sizes.items():
    if not size > 100000:
        sum += size

print(f"Sum of directores not over 100000: {sum}")

# -- Part Two --
space_avail = 70000000
update_space_needed = 30000000
space_needed = update_space_needed - (space_avail - dir_sizes[base_dir])
smol_size = 0
for dir, size in dir_sizes.items():
    if (size < smol_size or smol_size == 0) and size > space_needed:
        smol_size = size


print(f"Smallest directory size over 30000000: {smol_size}")