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

    compute_id = lambda x: x[0] * 8 + x[1]
    seats_id = list(map(compute_id, seats))

    print(f"PART1\nHighest seat_id: {max(seats_id)}")

    possible_seats = set((i, j) for i in range(128) for j in range(8))
    for seat in possible_seats - set(seats):
        seat_id = compute_id(seat)
        if seat_id - 1 in seats_id and seat_id + 1 in seats_id:
            break

    print(f"PART2\nYour seat_id: {seat_id}")


if __name__ == '__main__':
    execute()
