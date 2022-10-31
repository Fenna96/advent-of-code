import itertools
from time import perf_counter
import pandas as pd
import numpy as np
import re


def get_input():
    with open("9_12_2020/input.txt", "r") as input_file:
        return [int(n) for n in input_file.read().splitlines()]


def find_not_valid(preamble: list[int], code: list[int]):
    for x in code:
        lesser = [n for n in preamble if n < x]
        if not [(y, z) for y in lesser for z in lesser if y + z == x]:
            return x
        preamble.pop(0)
        preamble.append(x)


def find_weakness(numbers, not_valid):
    candidates = [x for x in numbers if x < not_valid]
    offset, subset_size = 0, 2

    while subset_size < len(candidates):
        while offset < len(candidates) - subset_size:
            subset = candidates[offset : offset + subset_size]
            if sum(subset) == not_valid:
                return min(subset) + max(subset)
            offset += 1

        subset_size += 1
        offset = 0


def execute():
    numbers = get_input()
    not_valid_number = find_not_valid(numbers[:25], numbers[25:])
    print(f"PART1\nNot valid number: {not_valid_number}")
    print(f"PART2\nCode weakness: {find_weakness(numbers, not_valid_number)}")


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
