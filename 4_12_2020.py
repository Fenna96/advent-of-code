import re


def get_input():
    with open('4_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def process_data(raw_data):
    processed_data = []
    current_processed_data = {}
    for row in raw_data:
        if not row:
            processed_data.append(current_processed_data)
            current_processed_data = {}
            continue
        for key_value in row.split():
            key, value = key_value.split(':')
            current_processed_data[key] = value
    current_processed_data and processed_data.append(current_processed_data)
    return processed_data


def validate_passport(passport):
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return fields.issubset(passport.keys())


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

    print(f"PART1\n{sum(map(validate_passport, passports))} valid passports")
    print(f"PART1\n{sum(map(validate_passport_and_fields, passports))} valid passports")


if __name__ == '__main__':
    execute()
