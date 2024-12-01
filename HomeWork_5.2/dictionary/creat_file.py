import json

def create_json_file(file_path, test_answer):
    with open(f'{file_path}.json', 'w', encoding='UTF-8') as file:
        json.dump(test_answer, file, indent=2)
    return file_path