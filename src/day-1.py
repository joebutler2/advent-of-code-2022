data = open("../input/day-1.txt", "r")

current = 0
max = 0
calories_by_elf = []
while True:
    line = data.readline()
    if line == "\n":
        calories_by_elf.append(current)
        current = 0
        continue
    if line == "":
        break
    current += int(line)
    max = current if current > max else max
data.close()

calories_by_elf.sort()
top_3 = calories_by_elf[-1:-4:-1]
print("Max value: " + str(max))
print(f"Top 3: {top_3[0]}, {top_3[1]}, {top_3[2]}")
print("Sum of top 3: " + str(sum(top_3)))
