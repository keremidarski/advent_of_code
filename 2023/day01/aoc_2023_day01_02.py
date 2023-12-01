# AOC 2023 Day 01 Part 01


string_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_result(input_file):
    result = 0

    with open(input_file) as file:
        for line in file.read().strip().split():
            digits = []

            for index, char in enumerate(line):
                if char.isdigit():
                    digits.append(char)
                
                for digit, value in enumerate(string_digits):
                    if line[index:].startswith(value):
                        digits.append(str(digit + 1))
            
            score = int(digits[0] + digits[-1])
            result += score

    return result


def main():
    input_file = "./day01.in"
    print(get_result(input_file))


if __name__ == "__main__":
    main()
            
