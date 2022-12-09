# AOC 2022 Day 09 Part 01


def prep_input():
    data = []

    with open("./day09.in") as file:
        for line in file.readlines():
            data.append(line.strip().split(" "))

    return data


def track_rope(data):
    visited = {(0, 0): 1}
    head = {"y": 0, "x": 0}
    tail = {"y": 0, "x": 0}
    y, x = 0, 0

    for move in data:
        if move[0] == "U":
            for i in range(int(move[1])):
                head["y"] += 1

                if abs(head["y"] - tail["y"]) > 1:
                    if head["x"] > tail["x"]:
                        tail["y"] += 1
                        tail["x"] += 1
                    elif head["x"] < tail["x"]:
                        tail["y"] += 1
                        tail["x"] -= 1
                    else:
                        tail["y"] += 1
                else:
                    continue

                if (tail["y"], tail["x"]) not in visited:
                    visited[(tail["y"], tail["x"])] = 1
                else:
                    visited[(tail["y"], tail["x"])] += 1

        elif move[0] == "D":
            for i in range(int(move[1])):
                head["y"] -= 1

                if abs(head["y"] - tail["y"]) > 1:
                    if head["x"] > tail["x"]:
                        tail["y"] -= 1
                        tail["x"] += 1
                    elif head["x"] < tail["x"]:
                        tail["y"] -= 1
                        tail["x"] -= 1
                    else:
                        tail["y"] -= 1
                else:
                    continue

                if (tail["y"], tail["x"]) not in visited:
                    visited[(tail["y"], tail["x"])] = 1
                else:
                    visited[(tail["y"], tail["x"])] += 1

        elif move[0] == "R":
            for i in range(int(move[1])):
                head["x"] += 1

                if abs(head["x"] - tail["x"]) > 1:
                    if head["y"] > tail["y"]:
                        tail["x"] += 1
                        tail["y"] += 1
                    elif head["y"] < tail["y"]:
                        tail["x"] += 1
                        tail["y"] -= 1
                    else:
                        tail["x"] += 1
                else:
                    continue

                if (tail["y"], tail["x"]) not in visited:
                    visited[(tail["y"], tail["x"])] = 1
                else:
                    visited[(tail["y"], tail["x"])] += 1

        elif move[0] == "L":
            for i in range(int(move[1])):
                head["x"] -= 1

                if abs(head["x"] - tail["x"]) > 1:
                    if head["y"] > tail["y"]:
                        tail["x"] -= 1
                        tail["y"] += 1
                    elif head["y"] < tail["y"]:
                        tail["x"] -= 1
                        tail["y"] -= 1
                    else:
                        tail["x"] -= 1
                else:
                    continue

                if (tail["y"], tail["x"]) not in visited:
                    visited[(tail["y"], tail["x"])] = 1
                else:
                    visited[(tail["y"], tail["x"])] += 1

    return visited


def main():
    data = prep_input()
    visited = track_rope(data)
    print(len(visited))


if __name__ == "__main__":
    main()
