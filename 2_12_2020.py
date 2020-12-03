import pandas as pd
import numpy as np


def get_input():
    with open('2_12_2020/input.txt', 'r') as input_file:
        passwords = input_file.readlines()
    passwords = [x.replace('\n', '') for x in passwords]
    return passwords


def parse_password(password: str):
    policy, password = password.split(':')
    delimiter, letter = policy.split(' ')
    lower, upper = delimiter.split('-')
    return int(lower), int(upper), letter, password.replace(' ', '')


def password_validator_first(password: str):
    lower, upper, letter, password = parse_password(password)
    return password.count(letter) in range(lower, upper + 1)


def password_validator_second(password: str):
    lower, upper, letter, password = parse_password(password)
    return (password[lower - 1] == letter) ^ (password[upper - 1] == letter)


def execute():
    passwords = get_input()
    count = {'first': [], 'second': []}
    for password in passwords:
        password_validator_first(password) and count['first'].append(1)
        password_validator_second(password) and count['second'].append(1)
    print(f"PART1\nFound {len(count['first'])} valid passwords.")
    print(f"PART2\nFound {len(count['second'])} valid passwords.")


if __name__ == '__main__':
    execute()
