# AOC 2022 Day 10 Part 01


def prep_input():
    data = []

    with open("./day10_demmo.in") as file:
        for line in file.readlines():
            data.append(line.strip().split())

    return data


def process_signal(data):
    signal = 0
    x = 1
    index = 0
    addx = {}

    for turn in range(1, 221):
        if addx:
            if addx["timer"] == 0:
                x += addx["add"]
                addx = {}
            else:
                addx["timer"] -= 1

        if turn in [20, 60, 100, 140, 180, 220]:
            signal += x * turn

        if not addx:
            if data[index][0] == "noop":
                index += 1
            else:
                addx["add"] = int(data[index][-1])
                addx["timer"] = 1
                index += 1

    return signal


def main():
    data = prep_input()
    tracked = process_signal(data)
    print(tracked)


if __name__ == "__main__":
    main()
