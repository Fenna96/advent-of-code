from dataclasses import dataclass, field
from functools import lru_cache
from time import perf_counter


_BAGS = {}


class BagMeta(type):
    def __call__(cls, *args, **kwargs):
        if args not in _BAGS:
            instance = super().__call__(*args, **kwargs)
            _BAGS[args] = instance
        return _BAGS[args]


@dataclass
class Bag(metaclass=BagMeta):
    tone: str
    color: str

    contain: dict = field(default_factory=dict)

    def __iter__(self):
        return iter((self.tone, self.color))


def get_input():
    with open("7_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


def process_data(raw_data):
    for line in raw_data:
        bag_string, contain_string = line.split(" bags contain ")
        bag = Bag(*bag_string.split(" "))
        if "no other bags" in contain_string:
            continue

        for contain_bag in contain_string.split(", "):
            count, tone, color = contain_bag.split(" ")[:3]
            bag.contain |= {tuple(Bag(tone, color)): int(count)}


@lru_cache
def can_contain(bag_tone: str, bag_color: str, search_tone: str, search_color: str):
    bag: Bag = _BAGS[(bag_tone, bag_color)]
    return any(
        [
            son == (search_tone, search_color)
            or can_contain(*son, search_tone, search_color)
            for son in bag.contain.keys()
        ]
    )


@lru_cache
def count_bag_sons(bag_tone: str, bag_color: str):
    bag: Bag = _BAGS[(bag_tone, bag_color)]
    return 1 + sum([count_bag_sons(*son) * count for son, count in bag.contain.items()])


def execute():
    raw_rules = get_input()
    process_data(raw_data=raw_rules)

    to_search = ("shiny", "gold")
    print(
        f"PART1\nBags that can contain: {sum([can_contain(*bag, *to_search) for bag in _BAGS.keys()])}"
    )
    print(
        f"PART2\nSons of shiny gold: {count_bag_sons(*to_search) - 1}"
    )  # '1' is the shiny bag


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
