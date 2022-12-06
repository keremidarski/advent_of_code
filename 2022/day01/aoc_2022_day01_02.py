# AOC 2022 Day 01 Puzzle 02

import re


def prep_input():
    dwarfs = []

    with open("input.txt", "r") as f:
        data = re.split("(?<!\.)\n\n", f.read())

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
