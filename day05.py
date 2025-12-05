import argparse


def load_data(file_path):

    ranges, ids = [], []
    with open(file_path, "r") as file:
        for line in file:
            if "-" in line:
                start, end = map(int, line.strip().split("-"))
                ranges.append((start, end))
            elif line.strip().isdigit():
                ids.append(int(line.strip()))

    return ranges, ids


def part1(input_file):

    ranges, ids = load_data(input_file)

    result = 0
    for id in ids:
        if is_in_ranges(id, ranges):
            result += 1

    return result


def part2(input_file):

    ranges, _ = load_data(input_file)
    final_ranges = []

    ranges = sorted(ranges, key=lambda x: x[0])
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            final_ranges.append((current_start, current_end))
            current_start, current_end = start, end

    final_ranges.append((current_start, current_end))

    return sum(end - start + 1 for start, end in final_ranges)


def is_in_ranges(id, ranges):
    for start, end in ranges:
        if start <= id <= end:
            return True
    return False


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    print("Part 1 solution:", part1(args.input_file))
    print("Part 2 solution:", part2(args.input_file))


if __name__ == "__main__":
    main()
