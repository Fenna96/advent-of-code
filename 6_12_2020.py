from collections import Counter
from time import perf_counter


def get_input():
    with open("6_12_2020/input.txt", "r") as input_file:
        return input_file.read().splitlines()


def process_data(raw_data):
    processed_data = []
    current_processed_data = Counter()

    def _save_current():
        nonlocal processed_data
        nonlocal current_processed_data

        if current_processed_data:
            processed_data.append(dict(current_processed_data))
            current_processed_data.clear()

    def _enrich_current(row: str):
        nonlocal current_processed_data

        current_processed_data["members"] += 1
        current_processed_data.update(Counter(row))

    for row in raw_data:
        if row:
            _enrich_current(row)
        else:
            _save_current()

    _save_current()
    return processed_data


def execute():
    raw_answers = get_input()
    answers = process_data(raw_answers)

    survey_result_any = Counter()
    survey_result_all = Counter()
    for answer in answers:
        for key in set(answer) - {"members"}:
            if answer[key] == answer["members"]:
                survey_result_all[key] += 1
            survey_result_any[key] += 1

    print(f"PART1\nSum counts: {sum(survey_result_any.values())}")
    print(f"PART2\nSum counts: {sum(survey_result_all.values())}")


if __name__ == "__main__":
    t1_start = perf_counter()
    execute()
    print(f"Exec time {perf_counter() - t1_start} seconds")
