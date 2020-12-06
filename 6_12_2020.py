from collections import Counter


def get_input():
    with open('6_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def process_data(raw_data):
    processed_data = []
    current_processed_data = Counter()
    for row in raw_data:
        if not row:
            processed_data.append(current_processed_data)
            current_processed_data = Counter()
            continue
        current_processed_data['members'] = current_processed_data.get('members', 0) + 1
        current_processed_data.update(Counter(row))
    current_processed_data and processed_data.append(current_processed_data)
    return processed_data


def execute():
    raw_answers = get_input()
    answers = process_data(raw_answers)

    survey_result_any = {}
    survey_result_all = {}
    for answer in answers:
        for key in set(answer.keys()) - set(['members']):
            if answer[key] == answer['members']:
                survey_result_all[key] = survey_result_all.get(key, 0) + 1
            survey_result_any[key] = survey_result_any.get(key, 0) + 1

    print(f"PART1\nSum counts: {sum(survey_result_any.values())}")
    print(f"PART2\nSum counts: {sum(survey_result_all.values())}")


if __name__ == '__main__':
    execute()
