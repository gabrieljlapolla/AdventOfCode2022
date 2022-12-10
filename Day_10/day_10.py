# Advent of Code 2022 - Day 10

with open('day_10_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

instructions = [l.strip() for l in lines] # Remove whitespace

X = 1 # Single register
cycle = 0 # CPU cycle counter
add_neXt = 0 # Value that needs to be added next cycle
signal_strengths = []

i = 0
while i < len(instructions):
    cycle += 1

    pixel_pos = cycle % 40 - 1 # Position on line to draw pixel

    if pixel_pos == 0: # New CRT line
        print()

    # Check what pixel should be drawn
    if X in [pixel_pos + n for n in range(-1, 2)]: # Lit
        print("#", end='')
    else: # Dark
        print('.', end='')

    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(X * cycle)

    if add_neXt == 0: # No value to be added this cycle
        step = instructions[i]
        if step != 'noop':
            # addx instruction
            add_neXt = int(step.split()[1]) # addx value
        else:
            i += 1 # Proceed to next instruction
    else:
        X += add_neXt
        add_neXt = 0
        i += 1 # Proceed to next instruction

print()
print(f"Sum of signal strengths: {sum(signal_strengths)}")
    