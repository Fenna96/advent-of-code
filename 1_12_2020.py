import pandas as pd
import numpy as np


def get_input():
    with open('1_12_2020/input.txt', 'r') as input_file:
        numbers = [int(x.strip()) for x in input_file.readlines()]
    return numbers


def find_sum_of_two(numbers, total=2020):
    # Complexity O(3n + n), asymptotic O(n)
    numbers_set = set(numbers)  # O(n)
    for number_x in numbers_set:  # O(n)
        number_y = total - number_x  # O(1)
        if number_y in numbers_set:  # O(1)
            return number_x * number_y  # O(1)


def find_sum_of_three(numbers, total=2020):
    # Complexity O(n * 3(n - 1) + n), asymptotic O(n^2)
    numbers_set = set(numbers)  # O(n)
    for x, number_x in enumerate(numbers):  # O(n)
        for number_y in numbers[x + 1:]:  # O(n - 1)
            number_z = total - number_x - number_y  # O(1)
            if number_z in numbers_set:  # O(1)
                return number_x * number_y * number_z  # O(1)


def execute():
    numbers = get_input()
    total = 2020
    result = find_sum_of_two(numbers=numbers, total=total)
    result and print(f"PART1\nFound two numbers that sum to {total}: {result}")
    result = find_sum_of_three(numbers=numbers, total=total)
    result and print(f"PART2\nFound three numbers that sum to {total}: {result}")


if __name__ == '__main__':
    execute()
