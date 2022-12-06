# AOC 2022 Day 01 Part 02


def prep_input():
    dwarfs = []

    with open("./day01.in") as file:
        data = file.read().split("\n\n")

    for dwarf in data:
        dwarfs.append([int(cal) for cal in dwarf.split("\n")])

    return dwarfs


def sum_calories(dwarfs):
    cal_sum = []

    for dwarf in dwarfs:
        cal_sum.append(sum(dwarf))

    return cal_sum


def top_three(dwarfs):
    sorted_dwarfs = sorted(dwarfs, reverse=True)

    return sorted_dwarfs[0] + sorted_dwarfs[1] + sorted_dwarfs[2]


def main():
    data = prep_input()
    cal_sum = sum_calories(data)
    result = top_three(cal_sum)
    print(result)


if __name__ == "__main__":
    main()
