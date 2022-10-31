from time import perf_counter


def get_input():
    with open("2_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


def parse_password(password: str):
    policy, password = password.split(": ")
    delimiter, letter = policy.split(" ")
    lower, upper = delimiter.split("-")
    return int(lower), int(upper), letter, password


def password_validator_first(password: str):
    lower, upper, letter, password = parse_password(password)
    return password.count(letter) in range(lower, upper + 1)


def password_validator_second(password: str):
    lower, upper, letter, password = parse_password(password)
    return (password[lower - 1] == letter) ^ (password[upper - 1] == letter)


def execute():
    passwords = get_input()

    print(
        f"PART1\nFound {sum(password_validator_first(pwd) for pwd in passwords)} valid passwords."
    )
    print(
        f"PART2\nFound {sum(password_validator_second(pwd) for pwd in passwords)} valid passwords."
    )


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
