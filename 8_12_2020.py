from dataclasses import dataclass, field
from functools import cached_property
from time import perf_counter


def increment(method):
    def wrapper(cpu: "CPU", *args, **kwargs):
        method(cpu, *args, **kwargs)
        cpu.ip += 1

    return wrapper


def get_input():
    with open("8_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


@dataclass
class CPU:
    instructions: list[tuple[str, int]]

    register: set[int] = field(init=False)
    ip: int = field(init=False)
    accumulator: int = field(init=False)

    _instructions: tuple[tuple[str, int]] = field(init=False)
    _corrected: int = field(init=False, default=0)

    def __post_init__(self):
        self._instructions = tuple(self.instructions)
        self._reset()

    @cached_property
    def nop_jump(self):
        return {
            self._instructions.index(instruction)
            for instruction in self._instructions
            if instruction[0] in ["jmp", "nop"]
        }

    @cached_property
    def corrector(self):
        return {"jmp": "nop", "nop": "jmp"}

    @increment
    def acc(self, value: int):
        self.accumulator += value

    @increment
    def jmp(self, value: int):
        self.ip += value - 1

    @increment
    def nop(self, _: int):
        pass

    def _reset(self):
        self.register = set()
        self.ip = 0
        self.accumulator = 0
        self.instructions[self._corrected] = self._instructions[self._corrected]

    def _run(self):
        operation, value = self.instructions[self.ip]
        self.register.add(self.ip)
        getattr(self, operation)(value)

    def _correct_instructions(self):
        index = self.nop_jump.pop()
        self.instructions[index] = (
            self.corrector[self._instructions[index][0]],
            self._instructions[index][1],
        )
        self._corrected = index

    def run_one(self):
        self._reset()
        while self.ip not in self.register:
            self._run()
        return self.accumulator

    def run_two(self):
        self._reset()
        while self.ip < len(self.instructions):
            if self.ip in self.register:
                self._reset()
                self._correct_instructions()
            else:
                self._run()
        return self.accumulator


def process_data(raw_data):
    instructions = []
    for line in raw_data:
        operation, value = line.split()
        instructions.append((operation, eval(value)))
    return instructions


def execute():
    raw_instructions = get_input()
    instructions = process_data(raw_instructions)
    program = CPU(instructions=instructions)
    print(f"PART1\nAccumulator value: {program.run_one()}")
    print(f"PART2\nAccumulator value: {program.run_two()}")


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
