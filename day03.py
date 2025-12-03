import argparse


def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    return data


def solve(input_file, n_digits=2):

    data = load_data(input_file)
    total = 0

    for line in data:
        number = ""
        for i in range(n_digits):

            digits = set(line)
            digits = sorted(digits, reverse=True)

            for digit in digits:
                max_index = line.find(digit)
                if max_index < (len(line) - n_digits + i + 1):
                    break

            line = line[max_index + 1 :]
            number += digit

        total += int(number)

    return total


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    print("Part 1 solution:", solve(args.input_file, n_digits=2))
    print("Part 2 solution:", solve(args.input_file, n_digits=12))


if __name__ == "__main__":
    main()
