def ask_question(word, translation):
    """Задаёт вопрос пользователю и возвращает результат ответа."""

    print(f"Переведите слово: {word.title()}")
    print("Подсказки: ")
    print(f"Это слово состоит из {len(translation)} букв")
    print(f"Первая буква слова: {translation[0].title()}\n")

    answer = input("Введите ваш ответ: ").replace(' ', '').lower()
    return answer == translation