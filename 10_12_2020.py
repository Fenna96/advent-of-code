def get_input():
    with open('10_12_2020/input.txt', 'r') as input_file:
        return [int(x.strip()) for x in input_file.readlines()]


def execute():
    numbers = get_input()
    raise NotImplementedError


if __name__ == '__main__':
    execute()
