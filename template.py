from time import perf_counter
import pandas as pd
import numpy as np
import re


def get_input():
    with open("_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


def execute():
    _ = get_input()
    raise NotImplementedError


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
