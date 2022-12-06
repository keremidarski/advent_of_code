# AOC 2022 Day 04 Part 01


def prep_input():
    pairs = []

    with open("./day04.in") as file:
        for line in file.read().splitlines():
            pair = []

            for interval in line.split(","):
                pair.append(interval.split("-"))

            pairs.append(pair)

    return pairs


def compare_pairs(pairs):
    overlaps = 0

    for pair in pairs:
        dwarf1 = [str(n) for n in range(int(pair[0][0]), int(pair[0][1]) + 1)]
        dwarf2 = [str(n) for n in range(int(pair[1][0]), int(pair[1][1]) + 1)]

        check1 = all(item in dwarf2 for item in dwarf1)
        check2 = all(item in dwarf1 for item in dwarf2)

        if check1 or check2:
            overlaps += 1

    return overlaps


def main():
    data = prep_input()
    overlaps = compare_pairs(data)
    print(overlaps)


if __name__ == "__main__":
    main()
