# AOC 2022 Day 07 Part 01


SIZES = {}


def prep_input():
    data = []

    with open("./day07.in") as file:
        for line in file.readlines():
            data.append(line.strip().split(" "))

    return data


def map_sizes(size, directory):
    if directory:
        levels = directory.copy()

        if "/".join(levels) not in SIZES:
            SIZES["/".join(levels)] = size
        else:
            SIZES["/".join(levels)] += size

        levels.pop()
        map_sizes(size, levels)


def scan_system(data):
    directory = []
    scanned = []

    for line in data:
        if "/" in line:
            directory = ["/"]
            continue

        if ".." in line:
            directory.pop()
            continue

        if "cd" in line:
            directory.append(line[-1])
            continue

        if "$" not in line and line[0].isnumeric():
            if directory in scanned:
                continue

            map_sizes(int(line[0]), directory)

    return SIZES


def get_result(sizes):
    result = 0

    for size in sizes.values():
        if size <= 100000:
            result += size

    return result


def main():
    data = prep_input()
    sizes = scan_system(data)
    result = get_result(sizes)
    print(result)


if __name__ == "__main__":
    main()
