import re
from time import perf_counter

RULES = {
    "byr": lambda x: re.match(r"^((19[2-9][0-9])|(200[0-2]))$", x),
    "iyr": lambda x: re.match(r"^((201[0-9])|2020)$", x),
    "eyr": lambda x: re.match(r"^((202[0-9])|2030)$", x),
    "hgt": lambda x: re.match(r"^((1[5-8][0-9])|(19[0-3]))cm$", x)
    or re.match(r"^((59)|(6[0-9])|(7[0-6]))in$", x),
    "hcl": lambda x: re.match(r"^#[a-f0-9]{6}$", x),
    "ecl": lambda x: re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x),
    "pid": lambda x: re.match(r"^[0-9]{9}$", x),
}


def get_input():
    with open("4_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


def process_data(raw_data: list[str]):
    processed_data = []
    current_processed_data = {}

    def _save_current():
        nonlocal processed_data
        nonlocal current_processed_data

        if current_processed_data:
            processed_data.append(current_processed_data)
            current_processed_data = {}

    def _enrich_current(row: str):
        nonlocal current_processed_data

        current_processed_data |= {
            k: v for k, v in [field.split(":") for field in row.split()]
        }

    for row in raw_data:
        if row:
            _enrich_current(row)
        else:
            _save_current()

    _save_current()
    return processed_data


def validate_passport(passport):
    return set(RULES).issubset(passport)


def validate_passport_and_fields(passport):
    return validate_passport(passport) and all(
        bool(verify(passport[rule])) for rule, verify in RULES.items()
    )


def execute():
    raw_passports = get_input()
    passports = process_data(raw_data=raw_passports)

    print(f"PART1\n{sum(map(validate_passport, passports))} valid passports")
    print(
        f"PART2\n{sum(map(validate_passport_and_fields, passports))} valid passports with valid fields"
    )


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
