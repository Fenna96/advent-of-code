import pandas as pd
import numpy as np


def get_input():
    with open('3_12_2020/input.txt', 'r') as input_file:
        chart = input_file.readlines()
    chart = [list(x.replace('\n', '')) for x in chart]
    return chart


class Navigator2D:
    def __init__(self, chart, movements, valuable):
        self.chart = chart
        self.right_delimiter = len(chart[0])
        self.move_right = movements['move_right']
        self.move_down = movements['move_down']
        self.position = [1, 1]
        self.valuable = valuable
        self.counter = 0

    def make_my_move(self):
        self.position[0] = (self.position[0] + self.move_right) % self.right_delimiter
        self.position[1] += self.move_down

    def evaluate_position(self):
        if self.proceed() and self.chart[self.position[1] - 1][self.position[0] - 1] == self.valuable:
            self.counter += 1

    def next(self):
        self.make_my_move()
        self.evaluate_position()

    def proceed(self):
        return self.position[1] <= len(self.chart)

    def reset(self, movements=None):
        self.position = [1, 1]
        self.counter = 0
        if movements:
            self.move_right = movements['move_right']
            self.move_down = movements['move_down']


def execute():
    nav = Navigator2D(
        chart=get_input(),
        movements={
            'move_right': 3,
            'move_down': 1
        },
        valuable='#'
    )

    while nav.proceed():
        nav.next()

    print(f"PART1\nMet {nav.counter} while moving")

    multiple_runs = [
        {'move_right': 1, 'move_down': 1},
        {'move_right': 3, 'move_down': 1},
        {'move_right': 5, 'move_down': 1},
        {'move_right': 7, 'move_down': 1},
        {'move_right': 1, 'move_down': 2}
    ]
    product = 1

    for run in multiple_runs:
        nav.reset(movements=run)
        while nav.proceed():
            nav.next()
        product *= nav.counter

    print(f"PART2\nTotal product of trees met: {product}")


if __name__ == '__main__':
    execute()
