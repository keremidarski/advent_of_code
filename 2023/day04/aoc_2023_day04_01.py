# AOC 2023 Day 04 Part 01


def get_result(input_file):
    result = 0

    with open(input_file) as file:
        for line in file.read().strip().split("\n"):
            points = 0
            winning_numbers = [
                int(num) for num in line.split(":")[-1].split("|")[0].split()
            ]
            numbers_to_check = [
                int(num) for num in line.split(":")[-1].split("|")[-1].split()
            ]

            for num in numbers_to_check:
                if num in winning_numbers:
                    if points == 0:
                        points += 1
                    else:
                        points *= 2

            result += points

    return result


def main():
    input_file = "/Users/administrator/code/misc/aoc/day04/day04.in"
    print(get_result(input_file))


if __name__ == "__main__":
    main()
