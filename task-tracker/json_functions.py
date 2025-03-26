import json
import os

file_path = 'tasks.json'

def get_json():
    """
    Create a file if doesn't exist and read a json file
    :return: list of dict
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    if not isinstance(data, list):
        data = [data]

    return data

def set_json(data):
    """
    Write data into a json file
    :param data: list of dict
    :return: None
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

