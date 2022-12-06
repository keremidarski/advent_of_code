# AOC 2022 Day 05 Part 01


def prep_input():
    matrix = []
    moves = []

    with open("./day05.in") as file:
        tasks = file.read().split("\n\n")
        diagram = tasks[0]
        steps = tasks[1]

    for line in diagram.splitlines():
        row = []

        for crate in range(1, len(line), 4):
            row.append(line[crate])

        matrix.append(row)

    for step in steps.split("\n"):
        move = []

        for word in step.split(" "):
            if word.isnumeric():
                move.append(word)

        moves.append(move)

    return matrix, moves


def move_crates(matrix, moves):
    result = ""

    for move in moves:
        repetitions = int(move[0])
        origin = int(move[1]) - 1
        destination = int(move[2]) - 1

        for repetition in range(repetitions):
            crate = ""

            for row in range(len(matrix)):
                if matrix[row][origin] == " ":
                    continue

                crate = matrix[row][origin]
                matrix[row][origin] = " "
                break

            if matrix[0][destination] != " ":
                matrix.insert(0, [" ", " ", " ", " ", " ", " ", " ", " ", " "])

            for row in range(len(matrix) - 1, -1, -1):
                if matrix[row][destination] != " ":
                    continue

                matrix[row][destination] = crate
                break

    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][column] == " ":
                continue

            result += matrix[row][column]
            break

    return result


def main():
    matrix, moves = prep_input()
    result = move_crates(matrix, moves)
    print(result)


if __name__ == "__main__":
    main()
