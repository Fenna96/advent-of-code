import pandas as pd
import numpy as np


def get_input():
    with open('3_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


class Navigator2D:
    def __init__(self, chart, movements, valuable):
        self.chart = chart
        self.x_delimiter = len(chart[0])
        self.move_x = movements['move_x']
        self.move_y = movements['move_y']
        self.valuable = valuable
        self.x = 1
        self.y = 1
        self.counter = 0

    def move(self):
        self.x = (self.x + self.move_x) % self.x_delimiter
        self.y += self.move_y
        if self.can_move() and self.chart[self.y - 1][self.x - 1] == self.valuable:
            self.counter += 1

    def can_move(self):
        return self.y <= len(self.chart)

    def restart(self, movements=None):
        self.x = 1
        self.y = 1
        self.counter = 0
        if movements:
            self.move_x = movements['move_x']
            self.move_y = movements['move_y']


def execute():
    nav = Navigator2D(
        chart=get_input(),
        movements={
            'move_x': 3,
            'move_y': 1
        },
        valuable='#'
    )

    while nav.can_move():
        nav.move()

    print(f"PART1\nMet {nav.counter} while moving")

    product = 1
    multiple_runs = [
        {'move_x': 1, 'move_y': 1},
        {'move_x': 3, 'move_y': 1},
        {'move_x': 5, 'move_y': 1},
        {'move_x': 7, 'move_y': 1},
        {'move_x': 1, 'move_y': 2}
    ]

    for run in multiple_runs:
        nav.restart(movements=run)
        while nav.can_move():
            nav.move()
        product *= nav.counter

    print(f"PART2\nTotal product of trees met: {product}")


if __name__ == '__main__':
    execute()
