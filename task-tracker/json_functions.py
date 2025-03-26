import json
import os

file_path = 'tasks.json'

def get_json():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Se o arquivo estiver vazio ou corrompido, começamos com uma lista vazia
    else:
        data = []

    # Garantimos que os dados sejam uma lista antes de adicionar o novo dado
    if not isinstance(data, list):
        data = [data]

    return data

def set_json(data):
    # Write data
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

