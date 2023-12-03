# AOC 2023 Day 03 Part 02


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


def sum_adjacent(scheme, point):
    digit_row, digit_column = point
    numbers = []
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

            if char_to_check.isdigit():
                numbers.append(get_number(scheme, (row, column)))

    unique = list(set(numbers))

    if len(unique) == 2:
        return unique[0] * unique[1]
    
    return 0


def get_number(scheme, point):
    digit_row, digit_column = point
    number = [scheme[digit_row][digit_column]]

    for option in [(digit_row, digit_column - 1), (digit_row, digit_column - 2)]:
        row, column = option
    
        if not out_of_bounds(scheme, option):
            current_char = scheme[row][column]
                    
            if current_char.isdigit():
                number.insert(0, current_char)
            else:
                break
        
    for option in [(digit_row, digit_column + 1), (digit_row, digit_column + 2)]:
        row, column = option
    
        if not out_of_bounds(scheme, option):
            current_char = scheme[row][column]
                    
            if current_char.isdigit():
                number.append(current_char)
            else:
                break
    
    return int("".join(number))  


def get_result(scheme):
    result = 0

    for row_index in range(len(scheme)):
        for column_index in range(len(scheme[0])):
            current_cell = scheme[row_index][column_index]

            if current_cell == "*":
                result += sum_adjacent(scheme, (row_index, column_index))
                
    return result


def main():
    input_file = "./day03.in"
    scheme = prep_input(input_file)

    print(get_result(scheme))


if __name__ == "__main__":
    main()
