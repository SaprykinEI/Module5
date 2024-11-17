from levels import get_words_by_level
from utils import ask_question
from rank import get_rank


def main():
    print("Уровни сложности: ")
    print("Легкий")
    print("Средений")
    print("Тяжелый\n")

    choice = input("Выберите уровень сложности: ").replace(' ', '').title()
    words = get_words_by_level(choice)


    answers = {}
    right = []
    incorrect = []
    counting_responses = 0


    for word, translation in words.items():
        if ask_question(word, translation):
            print(f"Верно, {word.title()} - это {translation}\n")
            answers[word] = True
            right.append(word)
            counting_responses += 1
        else:
            print(f"Неверно, {word.title()} - это {translation}\n")
            answers[word] = False
            incorrect.append(word)


    print(f'Вы правильно перевели слова: {', '.join(right).title()}')
    print(f'Вы неправильно перевели слова: {', '.join(incorrect).title()}')
    print(f"Ваш ранг: {get_rank(counting_responses)}")


if __name__ == "__main__":
    main()
