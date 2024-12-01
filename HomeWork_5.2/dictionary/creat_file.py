import json

def create_json_file(file, test_answer):
    with open(file, 'w', encoding='UTF-8') as file:
        json.dump(test_answer, file, indent=2)