# AOC 2022 Day 06 Part 01


def prep_input():
    with open("./day06.in") as file:
        signal = file.read()

    return signal


def get_marker(signal):
    result = 0
    combinations = []

    for i in range(len(signal) - 4):
        combinations = list(signal[i : i + 4])

        if len(combinations) != len(set(combinations)):
            continue

        result = i + 4
        break

    return result


def main():
    data = prep_input()
    result = get_marker(data)
    print(result)


if __name__ == "__main__":
    main()
