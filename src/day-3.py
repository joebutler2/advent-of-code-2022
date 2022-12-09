data = open("../input/day-3.txt", "r")
score = 0
def parse_rucksack(line: str):
    mid = len(line) // 2
    compartment = set(line[:mid])
    for item in line[mid:]:
        if item in compartment:
            return item


def score_item(item):
    ord_value = ord(item)
    if 65 <= ord_value <= 90:
        return ord_value - 38
    else:
        return ord_value - 96


while True:
    line = data.readline()
    if line == "":
        break
    dupe = parse_rucksack(line)
    print(f"Found dupe: {dupe}; value: {score_item(dupe)}")
    score += score_item(dupe)
data.close()

print("Score: " + str(score))