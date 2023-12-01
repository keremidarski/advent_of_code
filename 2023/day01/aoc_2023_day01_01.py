# AOC 2023 Day 01 Part 01


def get_result(input_file):
    result = 0

    with open(input_file) as file:
        for line in file.read().strip().split():
            digits = []

            for char in line:
                if char.isdigit():
                    digits.append(char)

            score = int(digits[0] + digits[-1])
            result += score

    return result


def main():
    input_file = "./day01.in"
    print(get_result(input_file))


if __name__ == "__main__":
    main()
            
