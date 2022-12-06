# AOC 2022 Day 02 Part 01


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

    if player == "X":
        score += 1

        if dwarf == "A":
            score += 3
        elif dwarf == "C":
            score += 6
    elif player == "Y":
        score += 2

        if dwarf == "A":
            score += 6
        elif dwarf == "B":
            score += 3
    elif player == "Z":
        score += 3

        if dwarf == "B":
            score += 6
        elif dwarf == "C":
            score += 3

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
