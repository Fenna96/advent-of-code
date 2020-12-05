import pandas as pd
import numpy as np
import re


def get_input():
    with open('4_12_2020/input.txt', 'r') as input_file:
        raw_passports = input_file.readlines()
    raw_passports = [x.strip() for x in raw_passports]
    return raw_passports


def process_data(raw_data):
    processed_datas = []
    current_processed_data = {}
    for row in raw_data:
        if not row:
            processed_datas.append(current_processed_data)
            current_processed_data = {}
            continue
        key_values = row.split()
        fields = {}
        for couple in key_values:
            key, value = couple.split(':')
            fields[key] = value
        current_processed_data.update(fields)
    processed_datas.append(current_processed_data)
    return processed_datas


def validate_passport(passport):
    fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return fields.issubset(set(passport.keys()))


def validate_fields(passport):
    rules = {
        'byr': lambda x: re.match(r"^((19[2-9][0-9])|(200[0-2]))$", x),
        'iyr': lambda x: re.match(r"^((201[0-9])|2020)$", x),
        'eyr': lambda x: re.match(r"^((202[0-9])|2030)$", x),
        'hgt': lambda x: re.match(r"^((1[5-8][0-9])|(19[0-3]))cm$", x) or re.match(r"^((59)|(6[0-9])|(7[0-6]))in$", x),
        'hcl': lambda x: re.match(r"^#[a-f0-9]{6}$", x),
        'ecl': lambda x: re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x),
        'pid': lambda x: re.match(r"^[0-9]{9}$", x),
    }

    valid = True
    for rule in rules.keys():
        valid = valid and bool(rules[rule](passport[rule]))
    return valid


def validate_passport_and_fields(passport):
    return validate_passport(passport=passport) and validate_fields(passport=passport)


def execute():
    raw_passports = get_input()
    passports = process_data(raw_data=raw_passports)

    count = []
    for passport in passports:
        validate_passport(passport=passport) and count.append(1)
    print(f"PART1\n{len(count)} valid passports")
    print()

    count = []
    for passport in passports:
        validate_passport_and_fields(passport=passport) and count.append(1)
    print(f"PART2\n{len(count)} valid passports")
    print()

if __name__ == '__main__':
    execute()
