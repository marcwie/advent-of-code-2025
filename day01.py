import argparse


def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    return [(-1 if line[0] == "L" else 1, int(line[1:])) for line in data]


def part1(input_file, position=50):

    data = load_data(input_file)
    result = 0

    for sign, value in data:
        position = (position + sign * value) % 100
        result += position == 0

    return result


def part2(input_file, position=50):

    data = load_data(input_file)
    result = 0

    for sign, value in data:

        new_position = position + sign * value

        if position == 0:
            result += value // 100
        elif sign == 1:
            result += new_position // 100
        elif sign == -1 and value >= position:
            result += abs(new_position) // 100 + 1

        position = new_position % 100

    return result


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    print("Part 1 solution:", part1(args.input_file))
    print("Part 2 solution:", part2(args.input_file))


if __name__ == "__main__":
    main()
