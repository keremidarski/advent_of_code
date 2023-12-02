# AOC 2023 Day 02 Part 02

import re


def prep_input(input_file):
    games = []

    with open(input_file) as file:
        for line in file.readlines():
            match = re.match(r"Game (\d+): (.+)", line)

            if match:
                game_number = int(match.group(1))
                color_counts = re.findall(r"(\d+) (\w+)", match.group(2))
                color_dict = {"game": game_number}

                for count, color in color_counts:
                    count = int(count)

                    if color in color_dict:
                        color_dict[color] = max(color_dict[color], count)
                    else:
                        color_dict[color] = count
                
                games.append(color_dict)

    return games


def count_games(games):
    result = 0
    
    for game in games:
        result += (game["blue"] * game["green"] * game["red"])

    return result



def main():
    input_file = "D:/Work/Code/Advent_of_Code/2023/day02/day02.in"
    games = prep_input(input_file)
    print(count_games(games))


if __name__ == "__main__":
    main()
          