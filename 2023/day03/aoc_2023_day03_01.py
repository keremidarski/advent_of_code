# AOC 2023 Day 03 Part 01

from pprint import pprint


def prep_input(input_file):
    scheme = []

    with open(input_file) as file:
        for line in file.read().strip().split("\n"):
            scheme.append(line)

    return scheme


def out_of_bounds(scheme, cell):
    x, y = cell

    MIN_X = 0
    MAX_X = len(scheme) - 1
    MIN_Y = 0
    MAX_Y = len(scheme[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def is_adjacent(scheme, current_number):
    digit_row, digit_column = current_number
    index_options = [
        (digit_row + 1, digit_column),
        (digit_row + 1, digit_column + 1),
        (digit_row + 1, digit_column - 1),
        (digit_row - 1, digit_column),
        (digit_row - 1, digit_column + 1),
        (digit_row - 1, digit_column - 1),
        (digit_row, digit_column + 1),
        (digit_row, digit_column - 1),
    ]

    for option in index_options:
        if not out_of_bounds(scheme, option):
            row, column = option
            char_to_check = scheme[row][column]

            if not char_to_check.isalnum() and char_to_check != ".":
                return True

    return False


def get_result(scheme):
    result = 0
    current_number = []
    still_number = False

    for row_index in range(len(scheme)):
        for column_index in range(len(scheme[0])):
            current_cell = scheme[row_index][column_index]

            if current_cell.isdigit():
                still_number = True
                current_number.append(
                    {"number": current_cell, "point": (row_index, column_index)}
                )
            else:
                if current_number:
                    whole_number = []
                    adjacent = False

                    for digit in current_number:
                        whole_number.append(digit["number"])

                        if is_adjacent(scheme, digit["point"]):
                            adjacent = True

                    if adjacent:
                        result += int("".join(whole_number))

                    current_number = []
                    adjacent = False

    return result


def main():
    input_file = "./day03.in"
    scheme = prep_input(input_file)

    print(get_result(scheme))


if __name__ == "__main__":
    main()
