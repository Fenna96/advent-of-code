import pandas as pd
import numpy as np


def get_input():
    with open('_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def execute():
    inputs = get_input()
    raise NotImplementedError


if __name__ == '__main__':
    execute()
