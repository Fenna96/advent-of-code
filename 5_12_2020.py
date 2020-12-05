import re


def get_input():
    with open('5_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def process_data(raw_data):
    raw_data = re.sub("[FL]", '0', raw_data)
    raw_data = re.sub("[BR]", '1', raw_data)
    return int(raw_data[:7], 2), int(raw_data[7:], 2)


def execute():
    raw_seats = get_input()
    seats = list(map(process_data, raw_seats))

    seats_id = list(map(lambda x: x[0] * 8 + x[1], seats))
    for seat in set((i, j) for i in range(128) for j in range(8)) - set(seats):
        seat_id = seat[0] * 8 + seat[1]
        if {seat_id - 1, seat_id + 1}.issubset(seats_id):
            break

    print(f"PART1\nHighest seatID: {max(seats_id)}")
    print(f"PART2\nYour seatID: {seat_id}")


if __name__ == '__main__':
    execute()
