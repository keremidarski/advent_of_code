# AOC 2023 Day 05 Part 01


def prep_input(input_file):
    almanac = {}
    data = []

    with open(input_file) as file:
        for line in file.read().strip().split("\n\n"):
            data.append(line)

    almanac["seeds"] = [int(x) for x in data[0].split(":")[-1].split()]
    almanac["seed_to_soil"] = [
        list(map(int, x))
        for x in [x.split() for x in data[1].split(":")[-1].split("\n") if x]
    ]
    almanac["soil_to_fertilizer"] = [
        list(map(int, x))
        for x in [x.split() for x in data[2].split(":")[-1].split("\n") if x]
    ]
    almanac["fertilizer_to_water"] = [
        list(map(int, x))
        for x in [x.split() for x in data[3].split(":")[-1].split("\n") if x]
    ]
    almanac["water_to_light"] = [
        list(map(int, x))
        for x in [x.split() for x in data[4].split(":")[-1].split("\n") if x]
    ]
    almanac["light_to_temperature"] = [
        list(map(int, x))
        for x in [x.split() for x in data[5].split(":")[-1].split("\n") if x]
    ]
    almanac["temperature_to_humidity"] = [
        list(map(int, x))
        for x in [x.split() for x in data[6].split(":")[-1].split("\n") if x]
    ]
    almanac["humidity_to_location"] = [
        list(map(int, x))
        for x in [x.split() for x in data[7].split(":")[-1].split("\n") if x]
    ]

    return almanac


def get_destination(seed, map):
    current = seed

    for ranges in map:
        destination = ranges[0]
        source = ranges[1]
        length = ranges[2]

        if source <= seed < source + length:
            current = destination + (seed - source)

    return current


def get_result(almanac):
    locations = []

    for seed in almanac["seeds"]:
        soil = get_destination(seed, almanac["seed_to_soil"])
        fertilizer = get_destination(soil, almanac["soil_to_fertilizer"])
        water = get_destination(fertilizer, almanac["fertilizer_to_water"])
        light = get_destination(water, almanac["water_to_light"])
        temperature = get_destination(light, almanac["light_to_temperature"])
        humidity = get_destination(temperature, almanac["temperature_to_humidity"])
        location = get_destination(humidity, almanac["humidity_to_location"])

        locations.append(location)

    return locations


def main():
    input_file = "./day05.in"
    almanac = prep_input(input_file)
    locations = get_result(almanac)
    print(sorted(locations)[0])


if __name__ == "__main__":
    main()
