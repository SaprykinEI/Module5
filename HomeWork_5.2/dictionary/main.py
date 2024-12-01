import json

from creat_file import create_json_file
from levels import get_user_level
from utils import base_program
from rank import get_rank



user_name = input("Здравствуйте, как вас зовут? ")


print("Уровни сложности: ")
print("Легкий")
print("Средений")
print("Тяжелый\n")

choice = input("Выберите уровень сложности: ").replace(' ', '').title()

test_words = get_user_level(choice)
test_answer = base_program(test_words)
result = get_rank(test_answer)

print(f"\nВаш ранг: {result}\n")


creating_json = create_json_file(user_name, test_answer)











