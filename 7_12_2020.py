import pandas as pd
import numpy as np
import re


class Bag:
    def __init__(self, color: str, tone: str, contain: list = None):
        self.color = color
        self.tone = tone
        self.contain = contain

    def __str__(self):
        return f"{self.tone} {self.color}"

    def get_contain(self):
        return self.contain

    def set_contain(self, contain):
        self.contain = contain


def get_input():
    with open('7_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def process_data(raw_data):
    bags = {}
    for line in raw_data:
        bag_string, contain_string = line.split('contain ')
        tone, color = bag_string.split(' ')[:2]
        bag_identifier = f"{tone} {color}"
        if bag_identifier not in bags:
            bag = Bag(color=color, tone=tone)
            bags[bag_identifier] = bag
        else:
            bag = bags[bag_identifier]

        bag_contain = {}
        contain_bags = contain_string.split(', ')
        for contain_bag in contain_bags:
            if 'no other bags' in contain_bag:
                break
            count, tone, color = contain_bag.split(' ')[:3]
            new_bag_identifier = f"{tone} {color}"
            if new_bag_identifier not in bags:
                new_bag = Bag(color=color, tone=tone)
                bags[new_bag_identifier] = new_bag
            else:
                new_bag = bags[new_bag_identifier]
            bag_contain[new_bag_identifier] = {
                'bag': new_bag,
                'count': int(count)
            }
        bag.set_contain(bag_contain)

    return bags


def can_contain(bag, contain: str = 'shiny gold'):
    if not bag.get_contain():
        return False

    can = False
    for bag in bag.get_contain().values():
        son_bag = bag['bag']
        if str(son_bag) == contain:
            return True
        can = can or can_contain(bag=son_bag)

    return can


def count_bag_sons(bag):
    if not bag.get_contain():
        return 1

    count = 1
    for son in bag.get_contain().values():
        count += count_bag_sons(bag=son['bag']) * son['count']

    return count


def execute():
    raw_rules = get_input()
    bags = process_data(raw_data=raw_rules)

    count = 0
    for bag in bags.values():
        if can_contain(bag=bag):
            count += 1
    print(f"PART1\nBags that can contain: {count}")
    print(f"PART2\nSons of shiny gold: {count_bag_sons(bags['shiny gold']) - 1}")  # '1' is the shiny bag


if __name__ == '__main__':
    execute()
