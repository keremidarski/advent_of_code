# AOC 2022 Day 08 Part 02


def prep_input():
    data = []

    with open("./day08.in") as file:
        for line in file.readlines():
            data.append(list(line.strip()))

    return data


def score(matrix, y, x):
    tree = matrix[y][x]
    up = 0
    down = 0
    left = 0
    right = 0

    if y > 0:
        for i in range(y - 1, -1, -1):
            up += 1

            if matrix[i][x] >= tree:
                break

    if y < len(matrix):
        for i in range(y + 1, len(matrix)):
            down += 1

            if matrix[i][x] >= tree:
                break

    if x > 0:
        for i in range(x - 1, -1, -1):
            left += 1

            if matrix[y][i] >= tree:
                break

    if x < len(matrix[0]):
        for i in range(x + 1, len(matrix[0])):
            right += 1

            if matrix[y][i] >= tree:
                break

    return up * down * left * right


def check_trees(matrix):
    top_score = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            current_score = score(matrix, y, x)

            if current_score > top_score:
                top_score = current_score

    return top_score


def main():
    data = prep_input()
    result = check_trees(data)
    print(result)


if __name__ == "__main__":
    main()
