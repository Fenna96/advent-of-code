from time import perf_counter


def get_input():
    with open("1_12_2020/input.txt", "r") as input_file:
        return set(int(x) for x in input_file.read().splitlines())


def find_sum_of_two(numbers: set, total: int = 2020):
    for number_x in numbers:
        if (number_y := total - number_x) in numbers:
            return number_x * number_y


def find_sum_of_three(numbers: set, total: int = 2020):
    while numbers:
        number_x = numbers.pop()
        internal_sum = find_sum_of_two(numbers, total - number_x)
        if internal_sum is not None:
            return number_x * internal_sum


def execute():
    total = 2020
    numbers = get_input()
    result = find_sum_of_two(numbers=numbers, total=total)
    print(f"PART1\nFound two numbers that sum to {total}: {result}")
    result = find_sum_of_three(numbers=numbers, total=total)
    print(f"PART2\nFound three numbers that sum to {total}: {result}")


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
