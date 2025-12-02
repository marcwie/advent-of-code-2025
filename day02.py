import argparse


def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.readline()
    data = [list(map(int, line.split("-"))) for line in data.split(",")]
    return data


def part1(input_file):

    data = load_data(input_file)
    total = 0

    for start, end in data:
        for candidate in range(start, end + 1):
            candidate_str = str(candidate)
            if candidate_str[: len(candidate_str) // 2] * 2 == candidate_str:
                total += candidate

    return total


def part2(input_file):

    data = load_data(input_file)
    total = 0

    for start, end in data:
        for candidate in range(start, end + 1):
            candidate_str = str(candidate)
            cand_len = len(candidate_str)
            for factor in range(1, cand_len // 2 + 1):
                if candidate_str[:factor] * (cand_len // factor) == candidate_str:
                    total += candidate
                    break

    return total


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    print("Part 1 solution:", part1(args.input_file))
    print("Part 2 solution:", part2(args.input_file))


if __name__ == "__main__":
    main()
