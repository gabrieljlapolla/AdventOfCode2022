# Advent of Code 2022 - Day 11

with open('day_11_input.txt', 'r') as input:
    lines = input.readlines() # Read in all lines

lines = [l.strip() for l in lines] # Remove whitespace

monkeys = {}
inspections = {}
rounds = 20

for i in range(0, len(lines), 7):
    monkey_num = int(i / 7)
    monkeys[monkey_num] = []
    inspections[monkey_num] = 0

    # Get items each monkey has
    items = lines[i + 1].split()[2:]
    items = [int(num[:-1]) if ',' in num else int(num) for num in items]
    monkeys[monkey_num].append(items)

    # Get operation
    operation = lines[i + 2].split()[-2:]
    monkeys[monkey_num].append(operation)

    test = lines[i + 3].split()[-3:] # Get test
    monkeys[monkey_num].append(test)
    if_true = lines[i + 4].split()[-1] # Get if true
    monkeys[monkey_num].append(int(if_true))
    if_false = lines[i + 5].split()[-1] # Get if false
    monkeys[monkey_num].append(int(if_false))


for i in range(1, rounds + 1):
    for monkey, attributes in monkeys.items():
        prev_items = attributes[0].copy()
        for item in prev_items:
            inspections[monkey] += 1
            worry_level = item
            operation = attributes[1][0]
            op_amt = attributes[1][1]

            if op_amt == 'old':
                op_amt = worry_level
            else:
                op_amt = int(op_amt)

            if operation == '*':
                worry_level = worry_level * op_amt
            elif operation == '+':
                worry_level = worry_level + op_amt

            # Update value
            worry_level //= 3

            test = attributes[2][0]
            test_amt = int(attributes[2][2])

            if test == 'divisible':
                if worry_level % test_amt == 0: # If true
                    throw_to = attributes[3]
                    monkeys[throw_to][0].append(worry_level)
                else: # If false
                    throw_to = attributes[4]
                    monkeys[throw_to][0].append(worry_level)

            # Remove item from current monkey
            monkeys[monkey][0].remove(item)

# Calculate monkey business by finding and multiply top two inspections
sorted_inspections = list(inspections.values())
sorted_inspections.sort()
monkey_business = sorted_inspections[-1] * sorted_inspections[-2]

print(f"Level of monkey business after {rounds} rounds: {monkey_business}")

