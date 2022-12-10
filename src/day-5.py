data = open("../input/day-5.txt", "r")

stacks = []
stack_lines = []
# First convert the raw table into a list of lists, then we can convert
# to a list of stacks to make it easier to work with.
for i in range(0, 8):
    line = data.readline()
    columns = []
    # 36 chars per line, 4 chars per column
    for j in range(0, 36, 4):
        chars = line[j:j + 4]
        chars = chars.translate({ord(c): None for c in '[]'}).strip()
        columns.append(chars if chars != "" else None)
    stack_lines.append(columns)

data.readline()  # Skip the column labels
data.readline()  # Skip the empty line

# Now convert the raw table into a list of stacks.
for col in range(0, 9):
    stack = []
    for row in range(7, -1, -1):
        cell = stack_lines[row][col]
        if cell is not None:
            stack.append(cell)
    stacks.append(stack)


while True:
    line = data.readline()
    if line == "":
        break
    # Instruction example: move 2 from 7 to 2
    instruction = line.split(" ")
    (count, source, destination) = [int(x) for x in instruction if x.rstrip().isdigit()]
    for i in range(0, count):
        stacks[destination - 1].append(stacks[source - 1].pop())
data.close()

print(f"Stacks: {stacks}")
top_crates = [stack.pop() for stack in stacks]
print(f"Top crates: {''.join(top_crates)}")
