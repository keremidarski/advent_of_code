# AOC 2022 Day 11 Part 01


def prep_input():
    sliced_monkeys = []
    monkeys = []

    with open("./day11.in") as file:
        for monkey in file.read().strip().split("\n\n"):
            sliced_monkeys.append(monkey)

    for monkey in sliced_monkeys:
        current_monkey = {"checked": 0}

        for line in monkey.split("\n"):

            if "Monkey" in line:
                continue

            if "Starting" in line:
                current_monkey["items"] = []

                for char in line.split():
                    if char.isnumeric():
                        current_monkey["items"].append(int(char))
                    elif "," in char:
                        current_monkey["items"].append(int(char[:-1]))
                continue

            if "Operation" in line:
                current_monkey["op"] = line.split("=")[-1].strip().split()
                continue

            if "Test" in line:
                current_monkey["test"] = int(line.split(":")[-1].strip().split()[-1])
                continue

            if "true" in line:
                current_monkey["true"] = int(line.split(":")[-1].strip()[-1])
                continue

            if "false" in line:
                current_monkey["false"] = int(line.split(":")[-1].strip()[-1])
                continue

        monkeys.append(current_monkey)

    return monkeys


def play(monkeys):
    checked = []

    for round in range(1, 21):
        for monkey in monkeys:
            for i in range(len(monkey["items"])):
                worry_level = monkey["items"][0]

                if monkey["op"][1] == "+":
                    if monkey["op"][-1] == "old":
                        worry_level += worry_level
                    else:
                        worry_level += int(monkey["op"][-1])

                if monkey["op"][1] == "*":
                    if monkey["op"][-1] == "old":
                        worry_level *= worry_level
                    else:
                        worry_level *= int(monkey["op"][-1])

                monkey["checked"] += 1
                worry_level //= 3

                if worry_level % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(worry_level)
                    monkey["items"].pop(0)
                else:
                    monkeys[monkey["false"]]["items"].append(worry_level)
                    monkey["items"].pop(0)

    for monkey in monkeys:
        checked.append(monkey["checked"])

    checked.sort(reverse=True)

    return checked[0] * checked[1]


def main():
    data = prep_input()
    result = play(data)
    print(result)


if __name__ == "__main__":
    main()
