# AOC 2022 Day 08 Part 01


def prep_input():
    data = []

    with open("./day08.in") as file:
        for line in file.readlines():
            data.append(list(line.strip()))

    return data


def is_visible(matrix, y, x):
    tree = matrix[y][x]
    visible = False

    for i in range(y - 1, -1, -1):
        if matrix[i][x] < tree:
            visible = True
            continue
        else:
            visible = False
            break

    if visible:
        return True

    for i in range(y + 1, len(matrix)):
        if matrix[i][x] < tree:
            visible = True
            continue
        else:
            visible = False
            break

    if visible:
        return True

    for i in range(x - 1, -1, -1):
        if matrix[y][i] < tree:
            visible = True
            continue
        else:
            visible = False
            break

    if visible:
        return True

    for i in range(x + 1, len(matrix[0])):
        if matrix[y][i] < tree:
            visible = True
            continue
        else:
            visible = False
            break

    if visible:
        return True

    return False


def count_visible(matrix):
    exterior_visible = (len(matrix) * 2) + (len(matrix[0]) * 2) - 4
    interior_visible = 0

    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if is_visible(matrix, y, x):
                interior_visible += 1

    return exterior_visible + interior_visible


def main():
    data = prep_input()
    result = count_visible(data)
    print(result)


if __name__ == "__main__":
    main()
