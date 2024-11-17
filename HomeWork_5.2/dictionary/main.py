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

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
    }


words = {}
answers = {}
right = []
incorrect = []
counting_responses = 0

print("Уровни сложности: ")
print("Легкий")
print("Средений")
print("Тяжелый\n")

choice = input("Выберите уровень сложности: ").replace(' ', '').title()

dif_level = ''

if choice == 'Легкий' or choice not in ['Легкий', 'Средний', 'Тяжелый']:
    dif_level = 'Легкий'
    print(f"Ваш уровень: {dif_level}\n")

    words = words_easy


elif choice == 'Средний':
    dif_level = 'Средний'
    print(f"Ваш уровень: {dif_level}\n")

    words = words_medium


elif choice == 'Тяжелый':
    dif_level = 'Тяжелый'
    print(f"Ваш уровень: {dif_level}\n")

    words = words_hard

for key, value in words.items():
    print(f"Переведите слово: {key.title()}")
    print("Подсказки: ")
    print(f"Это слово состоит из {len(value)} букв")
    print(f"Первая буква слова: {value[0].title()}\n")

    your_answer = input("Введите ваш ответ: ").replace(' ', '').lower()

    if your_answer == value:
        print(f"Верно, {key.title()} - это {value}\n")
        answers[key] = True
        right.append(key)
        counting_responses += 1
    else:
        print(f"Неверно, {key.title()} - это {value}\n")
        answers[key] = False
        incorrect.append(key)


print(f'Вы правильно перевели слова: {', '.join(right).title()}')
print(f'Вы неправильно перевели слова: {', '.join(incorrect).title()}')

for answer, level in levels.items():
    if counting_responses == answer:
        print(f'Ваш ранг: {level}')
