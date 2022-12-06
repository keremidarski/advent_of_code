# AOC 2022 Day 03 Part 02


def prep_input():
    with open("./day03.in") as file:
        data = file.read().splitlines()

    return data


def find_badges(data):
    badges = []
    group = []
    counter = 0

    for rucksack in data:
        if counter < 2:
            group.append(rucksack)
            counter += 1
        else:
            group.append(rucksack)

            dwarf1 = group[0]
            dwarf2 = group[1]
            dwarf3 = group[2]

            for item in dwarf1:
                if item in dwarf2 and item in dwarf3:
                    badges.append(item)
                    break

            group = []
            counter = 0

    return badges


def prioritize(badges):
    result = 0

    priorities = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }

    for badge in badges:
        result += priorities[badge]

    return result


def main():
    data = prep_input()
    badges = find_badges(data)
    result = prioritize(badges)
    print(result)


if __name__ == "__main__":
    main()
