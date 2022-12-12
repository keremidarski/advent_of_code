# AOC 2022 Day 12 Part 01


from string import ascii_lowercase
from heapq import heappop, heappush


def prep_input():
    grid = []

    with open("./day12.in") as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    return grid


grid = prep_input()
rows = len(grid)
columns = len(grid[0])


for y in range(rows):
    for x in range(columns):
        char = grid[y][x]

        if char == "S":
            start = y, x
        if char == "E":
            target = y, x


def get_height(letter):
    if letter in ascii_lowercase:
        return ascii_lowercase.index(letter)
    if letter == "S":
        return 0
    if letter == "E":
        return 25


def get_neighbours(y, x):
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        yy = y + dy
        xx = x + dx

        if not (0 <= yy < rows and 0 <= xx < columns):
            continue

        if get_height(grid[yy][xx]) <= get_height(grid[y][x]) + 1:
            yield yy, xx


visited = [[False] * columns for i in range(rows)]
heap = [(0, start[0], start[1])]

while True:
    steps, y, x = heappop(heap)

    if visited[y][x]:
        continue

    visited[y][x] = True

    if (y, x) == target:
        print(steps)
        break

    for yy, xx in get_neighbours(y, x):
        heappush(heap, (steps + 1, yy, xx))
