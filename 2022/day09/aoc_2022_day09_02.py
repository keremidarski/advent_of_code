# AOC 2022 Day 09 Part 02


def prep_input():
    data = []

    with open("./day09.in") as file:
        for line in file.readlines():
            data.append(line.strip().split(" "))

    return data


def track_rope(data):
    visited = {(0, 0): 1}
    rope = [
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
        {"y": 0, "x": 0},
    ]

    for move in data:
        if move[0] == "U":
            for i in range(int(move[1])):
                rope[0]["y"] += 1

                for knot in range(1, 10):
                    if (
                        abs(rope[knot - 1]["y"] - rope[knot]["y"]) > 1
                        or abs(rope[knot - 1]["x"] - rope[knot]["x"]) > 1
                    ):
                        if rope[knot - 1]["x"] > rope[knot]["x"]:
                            rope[knot]["x"] += 1
                        elif rope[knot - 1]["x"] < rope[knot]["x"]:
                            rope[knot]["x"] -= 1
                        if rope[knot - 1]["y"] > rope[knot]["y"]:
                            rope[knot]["y"] += 1
                        elif rope[knot - 1]["y"] < rope[knot]["y"]:
                            rope[knot]["y"] -= 1
                    else:
                        continue

                if (rope[-1]["y"], rope[-1]["x"]) not in visited:
                    visited[(rope[-1]["y"], rope[-1]["x"])] = 1
                else:
                    visited[(rope[-1]["y"], rope[-1]["x"])] += 1

        elif move[0] == "D":
            for i in range(int(move[1])):
                rope[0]["y"] -= 1

                for knot in range(1, 10):
                    if (
                        abs(rope[knot - 1]["y"] - rope[knot]["y"]) > 1
                        or abs(rope[knot - 1]["x"] - rope[knot]["x"]) > 1
                    ):
                        if rope[knot - 1]["x"] > rope[knot]["x"]:
                            rope[knot]["x"] += 1
                        elif rope[knot - 1]["x"] < rope[knot]["x"]:
                            rope[knot]["x"] -= 1
                        if rope[knot - 1]["y"] > rope[knot]["y"]:
                            rope[knot]["y"] += 1
                        elif rope[knot - 1]["y"] < rope[knot]["y"]:
                            rope[knot]["y"] -= 1
                    else:
                        continue

                if (rope[-1]["y"], rope[-1]["x"]) not in visited:
                    visited[(rope[-1]["y"], rope[-1]["x"])] = 1
                else:
                    visited[(rope[-1]["y"], rope[-1]["x"])] += 1

        elif move[0] == "R":
            for i in range(int(move[1])):
                rope[0]["x"] += 1

                for knot in range(1, 10):
                    if (
                        abs(rope[knot - 1]["y"] - rope[knot]["y"]) > 1
                        or abs(rope[knot - 1]["x"] - rope[knot]["x"]) > 1
                    ):
                        if rope[knot - 1]["x"] > rope[knot]["x"]:
                            rope[knot]["x"] += 1
                        elif rope[knot - 1]["x"] < rope[knot]["x"]:
                            rope[knot]["x"] -= 1
                        if rope[knot - 1]["y"] > rope[knot]["y"]:
                            rope[knot]["y"] += 1
                        elif rope[knot - 1]["y"] < rope[knot]["y"]:
                            rope[knot]["y"] -= 1
                    else:
                        continue

                if (rope[-1]["y"], rope[-1]["x"]) not in visited:
                    visited[(rope[-1]["y"], rope[-1]["x"])] = 1
                else:
                    visited[(rope[-1]["y"], rope[-1]["x"])] += 1

        elif move[0] == "L":
            for i in range(int(move[1])):
                rope[0]["x"] -= 1

                for knot in range(1, 10):
                    if (
                        abs(rope[knot - 1]["y"] - rope[knot]["y"]) > 1
                        or abs(rope[knot - 1]["x"] - rope[knot]["x"]) > 1
                    ):
                        if rope[knot - 1]["x"] > rope[knot]["x"]:
                            rope[knot]["x"] += 1
                        elif rope[knot - 1]["x"] < rope[knot]["x"]:
                            rope[knot]["x"] -= 1
                        if rope[knot - 1]["y"] > rope[knot]["y"]:
                            rope[knot]["y"] += 1
                        elif rope[knot - 1]["y"] < rope[knot]["y"]:
                            rope[knot]["y"] -= 1
                    else:
                        continue

                if (rope[-1]["y"], rope[-1]["x"]) not in visited:
                    visited[(rope[-1]["y"], rope[-1]["x"])] = 1
                else:
                    visited[(rope[-1]["y"], rope[-1]["x"])] += 1

    return visited


def main():
    data = prep_input()
    visited = track_rope(data)
    print(len(visited))


if __name__ == "__main__":
    main()
