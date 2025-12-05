import argparse

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    data = [list(line) for line in data]
    return data


def get_coordinates(data):
    positions = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                positions.add((i, j))
    return positions


def part1(input_file):

    data = load_data(input_file)
    positions = get_coordinates(data)
    result = 0

    for x, y in positions:
        neighbors = sum(1 for dx, dy in DIRECTIONS if (x + dx, y + dy) in positions)
        result += neighbors < 4

    return result


def part2(input_file):

    data = load_data(input_file)
    positions = get_coordinates(data)
    result = 0

    while True:
        removed = set()
        for x, y in positions:
            neighbors = sum(1 for dx, dy in DIRECTIONS if (x + dx, y + dy) in positions)
            if neighbors < 4:
                result += 1
                removed.add((x, y))

        if not removed:
            break
        positions -= removed

    return result


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    print("Part 1 solution:", part1(args.input_file))
    print("Part 2 solution:", part2(args.input_file))


if __name__ == "__main__":
    main()
