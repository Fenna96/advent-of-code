from dataclasses import dataclass, field
from functools import cached_property
from typing import NamedTuple


def get_input():
    with open("3_12_2020/input.txt", "r") as input_file:
        return [x.strip() for x in input_file.readlines()]


class Movement(NamedTuple):
    move_x: int
    move_y: int


@dataclass
class Navigator2D:
    chart: list[str]
    valuable: str

    movement: Movement = field(init=False)
    x: int = field(init=False)
    y: int = field(init=False)
    counter: int = field(init=False)

    @cached_property
    def x_delimiter(self):
        return len(self.chart[0])

    @property
    def current_position(self):
        return self.chart[self.y][self.x]

    @property
    def valid_position(self):
        return self.y < len(self.chart)

    @property
    def valuable_position(self):
        return self.valid_position and self.current_position == self.valuable

    def _move(self):
        self.x = (self.x + self.movement.move_x) % self.x_delimiter
        self.y += self.movement.move_y
        self.counter += self.valuable_position

    def _setup(self, move: Movement):
        self.x = self.y = self.counter = 0
        self.movement = move

    def _run(self):
        while self.valid_position:
            self._move()

    def execute(self, move: Movement):
        self._setup(move)
        self._run()
        return self.counter


def execute():
    nav = Navigator2D(chart=get_input(), valuable="#")
    result = nav.execute(run=Movement(3, 1))
    print(f"PART1\nMet {result} while moving")

    product = 1
    movements = [
        Movement(1, 1),
        Movement(3, 1),
        Movement(5, 1),
        Movement(7, 1),
        Movement(1, 2),
    ]
    for move in movements:
        product *= nav.execute(move)

    print(f"PART2\nTotal product of trees met: {product}")


if __name__ == "__main__":
    execute()
