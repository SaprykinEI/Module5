levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
    }

def get_rank(answers, levels):
    """Возвращает ранг пользователя на основе правильных ответов."""

    rank = ''
    counting_responses = 0

    for correct in answers.values():
        if correct:
            counting_responses += 1

    print(answers)

    for answer, level in levels.items():
        if counting_responses == answer:
            rank = level

    return rank