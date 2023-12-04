# AOC 2023 Day 04 Part 02


def prep_input(input_file):
    games = []

    with open(input_file) as file:
        for line in file.read().strip().split("\n"):
            game_number = int(line.split(":")[0].split("Card ")[-1])
            winning_numbers = [
                int(num) for num in line.split(":")[-1].split("|")[0].split()
            ]
            numbers_to_check = [
                int(num) for num in line.split(":")[-1].split("|")[-1].split()
            ]

            games.append(
                {
                    f"game_{game_number}": {
                        "copies": 0,
                        "winning_numbers": winning_numbers,
                        "numbers_to_check": numbers_to_check,
                    }
                }
            )

    return games


def count_cards(games):
    count = 0

    for index, game in enumerate(games):
        matches = 0
        current_game = index + 1

        for number in game[f"game_{current_game}"]["numbers_to_check"]:
            if number in game[f"game_{current_game}"]["winning_numbers"]:
                matches += 1

        for match in range(1, matches + 1):
            games[current_game + match - 1][f"game_{current_game + match}"][
                "copies"
            ] += (1 + game[f"game_{current_game}"]["copies"])

        count += game[f"game_{current_game}"]["copies"] + 1

    return count


def main():
    input_file = "./day04.in"
    games = prep_input(input_file)
    count = count_cards(games)
    print(count)


if __name__ == "__main__":
    main()
