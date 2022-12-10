# AOC 2022 Day 10 Part 02


def prep_input():
    data = []

    with open("./day10.in") as file:
        for line in file.readlines():
            data.append(line.strip().split())

    return data


def process_signal(data):
    x = 1
    index = 0
    addx = {}
    drawing = []
    line = []
    crt = -1

    for turn in range(1, 241):
        if addx:
            if addx["timer"] == 0:
                x += addx["add"]
                addx = {}
            else:
                addx["timer"] -= 1

        crt += 1

        if abs(crt - x) < 2:
            line.append("#")
        else:
            line.append(".")

        if turn in [40, 80, 120, 160, 200, 240]:
            drawing.append(line)
            line = []
            crt = -1

        if not addx:
            if data[index][0] == "noop":
                index += 1
            else:
                addx["add"] = int(data[index][-1])
                addx["timer"] = 1
                index += 1

    return drawing


def main():
    data = prep_input()
    result = process_signal(data)

    for line in result:
        print("".join(line))


if __name__ == "__main__":
    main()
