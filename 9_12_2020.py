import pandas as pd
import numpy as np
import re


def get_input():
    with open('9_12_2020/input.txt', 'r') as input_file:
        return [int(x.strip()) for x in input_file.readlines()]


def find_not_valid(preamble, code):
    for i, x in enumerate(code):
        if not [(y, z) for y in preamble for z in preamble if y + z == x]:
            return x
        preamble = preamble[1:] + [code[i]]


def find_weakness(numbers, not_valid):
    numbers = [x for x in numbers if x < not_valid]
    for i, x in enumerate(numbers):
        for n in range(i):
            subset = numbers[n:i + 1]
            if len(subset) > 1 and sum(subset) == not_valid:
                return min(subset) + max(subset)


def execute():
    numbers = get_input()
    not_valid_number = find_not_valid(numbers[:25], numbers[25:])
    print(f"PART1\nNot valid number: {not_valid_number}")
    print(f"PART2\nCode weakness: {find_weakness(numbers, not_valid_number)}")


if __name__ == '__main__':
    execute()
