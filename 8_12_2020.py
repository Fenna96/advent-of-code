import pandas as pd
import numpy as np
import re
import copy


def get_input():
    with open('8_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


class CPU:
    def __init__(self, instructions):
        self.accumulator = 0
        self.ip = 0
        self.operations = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }
        self.instructions = instructions
        self.modified_instructions = copy.deepcopy(instructions)
        self.register = []
        self.nop_jump = [instructions.index(instruction) for instruction in instructions if instruction[0] in ['jmp', 'nop']]

    def acc(self, value):
        self.accumulator += value
        self.ip += 1

    def jmp(self, value):
        self.ip += value

    def nop(self, value):
        self.ip += 1

    def reset(self):
        self.register = []
        self.ip = 0
        self.accumulator = 0
        self.modified_instructions = copy.deepcopy(self.instructions)

    def run_one(self):
        self.reset()
        while self.ip not in self.register:
            operation, value = self.instructions[self.ip]
            self.register.append(self.ip) or self.operations[operation](value)
        return self.accumulator

    def correct_instructions(self, exclude):
        self.reset()
        index = min(set(self.nop_jump) - set(exclude))
        self.modified_instructions[index] = ('jmp' if self.modified_instructions[index][0] == 'nop' else 'nop',
                                             self.modified_instructions[index][1])
        return index

    def run_two(self):
        self.reset()
        correction_tries = []
        while self.ip != len(self.modified_instructions):
            if self.ip in self.register:
                correction_tries.append(self.correct_instructions(correction_tries))
                continue
            operation, value = self.modified_instructions[self.ip]
            self.register.append(self.ip) or self.operations[operation](value)
        return self.accumulator


def process_data(raw_data):
    instructions = []
    for line in raw_data:
        operation, raw_value = line.split()
        value = int(raw_value[1:]) * (-1) if raw_value[0] == '-' else int(raw_value[1:])
        instructions.append((operation, value))
    return instructions


def execute():
    raw_instructions = get_input()
    instructions = process_data(raw_instructions)
    program = CPU(instructions=instructions)
    print(f"PART1\nAccumulator value: {program.run_one()}")
    print(f"PART2\nAccumulator value: {program.run_two()}")


if __name__ == '__main__':
    execute()
