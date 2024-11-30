import json

from levels import get_user_level
from utils import base_program
from rank import get_rank, levels


user_name = input("Здравствуйте, как вас зовут? ")


print("Уровни сложности: ")
print("Легкий")
print("Средений")
print("Тяжелый\n")

choice = input("Выберите уровень сложности: ").replace(' ', '').title()

test_words = get_user_level(choice)
test_answer = base_program(test_words)
result = get_rank(test_answer, levels)
print(f"\nВаш ранг: {result}\n")


with open(user_name, 'w', encoding='UTF-8') as file:
    json.dump(test_answer, file, indent=2)



