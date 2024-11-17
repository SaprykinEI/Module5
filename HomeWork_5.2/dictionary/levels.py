words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
    }

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
    }

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
    }


def get_words_by_level(choice):
    """Возвращает слова и уровень сложности на основе выбора."""

    if choice == 'Средний':
        print(f"Ваш уровень: 'Средний'\n")
        return words_medium

    elif choice == 'Тяжелый':
        print(f"Ваш уровень: 'Тяжелый'\n")
        return words_hard

    else:
        print("Ваш уровень Лёгкий\n")
        return words_easy