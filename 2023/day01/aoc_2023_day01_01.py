# AOC 2023 Day 01 Part 01


def prep_input(input_file):
    codes = []

    with open(input_file) as file:
        for line in file.read().strip().split():
            numbers = []
            
            for char in line:
                if char.isdigit():
                    numbers.append(char)

            if len(numbers) == 1:
                codes.append(int(numbers[0] + numbers[0]))
            else:
                codes.append(int(numbers[0] + numbers[-1]))

    return codes


def main():
    input_file = "./day01.in"
    codes = prep_input(input_file)
    print(sum(codes))


if __name__ == "__main__":
    main()
  
