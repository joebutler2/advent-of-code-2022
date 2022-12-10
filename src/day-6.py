data = open("../input/day-6.txt", "r")

unique_index = 0
unique_count = 0
unique_chars = set()
counter = 0

line = data.readline()
previous_char = None
for char in line:
    if char != previous_char and char not in unique_chars:
        unique_count += 1
        if unique_count == 4:
            print(f"Index: {unique_index + 4}")
            break
        unique_chars.add(char)
        previous_char = char
    else:
        unique_chars.clear()
        unique_count = 0
        previous_char = char
        unique_index = counter
    counter += 1

