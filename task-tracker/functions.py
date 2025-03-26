"""
Task Properties:
    - id
    - description
    - status (todo, in-progress, done)
    - createdAt
    - updatedAt
"""
import json_functions as jf
from datetime import datetime


def add(description):
    data = jf.get_json()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {
        "id": data[-1]["id"] + 1 if data else 0,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
        }

    data.append(task)
    jf.set_json(data)


def update_task(id, desc):
    data = jf.get_json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for task in data:
        if task["id"] == id:
            task["description"] = desc
            task["updatedAt"] = now
            jf.set_json(data)
            return
    else:
        print(f'Task {id} não encontrada!')


def delete(id):
    data = jf.get_json()

    filtered_data = [item for item in data if item.get("id") != id]

    if len(data) == len(filtered_data):
        print(f'Task {id} não encontrada!')
    else:
        jf.set_json(filtered_data)


def update_status(status, id):
    data = jf.get_json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for task in data:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = now
            jf.set_json(data)
            return
    else:
        print(f'Task {id} não encontrada!')


def list_tasks(filter=False):
    data = jf.get_json()
    if filter:
        for task in data:
            if task["status"] == filter:
                print(task)
    else:
        print(data)

