from enum import Enum

data = open("../input/day-2.txt", "r")

Shape = Enum('Shape', 'Rock Paper Scissors')

score = 0


def score_moves(opponent: Shape, me: Shape) -> int:
    if me == Shape.Rock:
        base = 1
    elif me == Shape.Paper:
        base = 2
    elif me == Shape.Scissors:
        base = 3

    if opponent == me:
        return base + 3
    elif opponent == Shape.Rock:
        return base + 6 if me == Shape.Paper else base
    elif opponent == Shape.Paper:
        return base + 6 if me == Shape.Scissors else base
    elif opponent == Shape.Scissors:
        return base + 6 if me == Shape.Rock else base
    else:
        raise ValueError("Invalid score")


# Used directly for part 1
def convert_move(move: str) -> Shape:
    if move == "A" or move == "X":
        return Shape.Rock
    elif move == "B" or move == "Y":
        return Shape.Paper
    elif move == "C" or move == "Z":
        return Shape.Scissors
    else:
        raise ValueError("Invalid move")

# Only used for part 2
def plan_my_move(opponent: str, me: str) -> (Shape, Shape):
    opponent_move = convert_move(opponent)
    if me == "X": # Lose
        if opponent_move == Shape.Rock:
            return Shape.Scissors
        elif opponent_move == Shape.Paper:
            return Shape.Rock
        elif opponent_move == Shape.Scissors:
            return Shape.Paper
    elif me == "Y": # Draw
        return opponent_move
    elif me == "Z": # Win
        if opponent_move == Shape.Rock:
            return Shape.Paper
        elif opponent_move == Shape.Paper:
            return Shape.Scissors
        elif opponent_move == Shape.Scissors:
            return Shape.Rock

while True:
    line = data.readline()
    if line == "":
        break
    (opponent, me) = line.rstrip().split(" ")
    my_move = plan_my_move(opponent, me)
    score += score_moves(convert_move(opponent), my_move)
data.close()

print("score: " + str(score))
