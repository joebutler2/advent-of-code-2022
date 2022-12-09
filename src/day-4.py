data = open("../input/day-4.txt", "r")
overlap_count = 0


def extract_range_set(elf_1):
    elf_1_range = elf_1.split("-")
    return set(range(int(elf_1_range[0]), int(elf_1_range[1]) + 1))


while True:
    line = data.readline()
    if line == "":
        break
    elf_1, elf_2 = line.split(",")
    first_range = extract_range_set(elf_1)
    second_range = extract_range_set(elf_2)
    if first_range.issubset(second_range) or second_range.issubset(first_range):
        overlap_count += 1
data.close()

print("Score: " + str(overlap_count))
