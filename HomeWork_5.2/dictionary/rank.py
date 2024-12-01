import json


def get_rank(answers):
    """Возвращает ранг пользователя на основе правильных ответов."""

    with open('questions.json', 'r', encoding='utf-8') as file:
        data_level = json.load(file)


    level_data = data_level[1]["levels"]

    rank = ''
    counting_responses = 0

    for correct in answers.values():
        if correct:
            counting_responses += 1

    print(answers)

    for number, level in level_data.items():
        if counting_responses == int(number):
            rank = level


    return rank

