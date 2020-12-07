import pandas as pd
import numpy as np
import re


class Bag:
    def __init__(self, color: str, tone: str):
        self.color = color
        self.tone = tone
        self.contain = {}

    def __str__(self):
        return f"{self.tone} {self.color}"

    def get_contain(self):
        return self.contain

    def set_contain(self, contain):
        self.contain = contain


def get_input():
    with open('7_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def register_bag(tone: str, color: str, bags: dict):
    bag_identifier = f"{tone} {color}"
    if bag_identifier not in bags:
        bag = Bag(color=color, tone=tone)
        bags[bag_identifier] = bag
    else:
        bag = bags[bag_identifier]
    return bag


def process_data(raw_data):
    bags = {}
    for line in raw_data:
        bag_string, contain_string = line.split('contain ')
        tone, color = bag_string.split(' ')[:2]
        bag = register_bag(tone=tone, color=color, bags=bags)
        for contain_bag in [x for x in contain_string.split(', ') if 'no other bags' not in x]:
            count, tone, color = contain_bag.split(' ')[:3]
            new_bag = register_bag(tone=tone, color=color, bags=bags)
            bag.get_contain().update({str(new_bag): {'bag': new_bag, 'count': int(count)}})

    return bags


def can_contain(bag, contain: str = 'shiny gold'):
    return any([str(son['bag']) == contain or can_contain(bag=son['bag']) for son in bag.get_contain().values()])


def count_bag_sons(bag):
    return 1 + sum([count_bag_sons(bag=son['bag']) * son['count'] for son in bag.get_contain().values()])


def execute():
    raw_rules = get_input()
    bags = process_data(raw_data=raw_rules)

    print(f"PART1\nBags that can contain: {sum([1 if can_contain(bag=bag) else 0 for bag in bags.values()])}")
    print(f"PART2\nSons of shiny gold: {count_bag_sons(bags['shiny gold']) - 1}")  # '1' is the shiny bag


if __name__ == '__main__':
    execute()
