from functools import lru_cache
from time import perf_counter


def get_input():
    with open("5_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


@lru_cache
def _value_to_binary(val: str):
    return str(int(val in ["B", "R"]))


@lru_cache
def _binary_to_int(binary: str):
    return int(binary, 2)


@lru_cache
def _id(first: int, second: int):
    return first * 8 + second


def process_data(raw_data):
    data = "".join([_value_to_binary(v) for v in raw_data])
    return _binary_to_int(data[:7]), _binary_to_int(data[7:])


def execute():
    raw_seats = get_input()
    seats = set(map(process_data, raw_seats))
    seats_id = set(_id(*seat) for seat in seats)

    print(f"PART1\nHighest seatID: {max(seats_id)}")

    candidates = set((i, j) for i in range(128) for j in range(8)) - seats
    for seat in candidates:
        seat_id = _id(*seat)
        if {seat_id - 1, seat_id + 1} - seats_id:
            break

    print(f"PART2\nYour seatID: {seat_id}")


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
