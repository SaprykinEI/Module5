import json


def get_user_level(choice):
    """Возвращает слова и уровень сложности на основе выбора."""

    with open('questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    questions = data[0]["questions"]

    words_easy = questions[0]
    words_medium = questions[1]
    words_hard = questions[2]

    if choice == 'Средний':
        print(f"Ваш уровень: 'Средний'\n")
        return words_medium

    elif choice == 'Тяжелый':
        print(f"Ваш уровень: 'Тяжелый'\n")
        return words_hard

    else:
        print("Ваш уровень Лёгкий\n")
        return words_easy