import pandas as pd
import numpy as np
import re


def get_input():
    with open('6_12_2020/input.txt', 'r') as input_file:
        return [x.strip() for x in input_file.readlines()]


def process_data(raw_data):
    processed_data = []
    current_processed_data = {}
    for row in raw_data:
        if not row:
            processed_data.append(current_processed_data)
            current_processed_data = {}
            continue
        current_processed_data['members'] = current_processed_data.get('members', 0) + 1
        for letter in row:
            current_processed_data[letter] = current_processed_data.get(letter, 0) + 1
    current_processed_data and processed_data.append(current_processed_data)
    return processed_data


def execute():
    raw_answers = get_input()
    answers = process_data(raw_answers)

    survey_result = {}
    for answer in answers:
        for key in set(answer.keys()) - set(['members']):
            survey_result[key] = survey_result.get(key, 0) + 1

    print(f"PART1\nSum counts: {sum(survey_result.values())}")

    survey_result = {}
    for answer in answers:
        for key in set(answer.keys()) - set(['members']):
            if answer[key] == answer['members']:
                survey_result[key] = survey_result.get(key, 0) + 1

    print(f"PART2\nSum counts: {sum(survey_result.values())}")


if __name__ == '__main__':
    execute()
