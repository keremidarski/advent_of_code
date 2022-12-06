# AOC 2022 Day 02 Part 02


def prep_input():
    moves = []

    with open("./day02.in") as file:
        data = file.read().splitlines()

    for move in data:
        moves.append(move.split())

    return moves


def rock_paper_scissors(move):
    dwarf = move[0]
    player = move[1]

    score = 0

    if dwarf == "A":
        if player == "X":
            score += 3
        elif player == "Y":
            score += 4
        elif player == "Z":
            score += 8
    elif dwarf == "B":
        if player == "X":
            score += 1
        elif player == "Y":
            score += 5
        elif player == "Z":
            score += 9
    elif dwarf == "C":
        if player == "X":
            score += 2
        elif player == "Y":
            score += 6
        elif player == "Z":
            score += 7

    return score


def calc_score(moves):
    result = 0

    for move in moves:
        result += rock_paper_scissors(move)

    return result


def main():
    data = prep_input()
    result = calc_score(data)
    print(result)


if __name__ == "__main__":
    main()
