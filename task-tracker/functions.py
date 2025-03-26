"""
Task Properties:
    - id: A unique identifier for the task
    - description: A short description of the task
    - status: The status of the task (todo, in-progress, done)
    - createdAt: The date and time when the task was created
    - updatedAt: The date and time when the task was last updated
"""
import json_functions as jf
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style


def add(description):
    """
    Adds new tasks into tracker and json file
    :param description: a task property
    :return: a list with all the task, including the new task
    """
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
    print(Fore.GREEN + f"Task {task['id']} added successfully!" + Style.RESET_ALL)
    list_tasks()

def update_task(id, desc):
    """
    Updates the description of some task
    :param id: indicates the task to update
    :param desc: the new description of the task
    :return: a list with all the task or an error if the task doesn't exist
    """
    data = jf.get_json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for task in data:
        if task["id"] == id:
            task["description"] = desc
            task["updatedAt"] = now
            jf.set_json(data)
            print(Fore.GREEN + f"Task {task['id']} updated successfully!" + Style.RESET_ALL)
            list_tasks()
            return
    else:
        print(Fore.RED + f"Task {id} not found!" + Style.RESET_ALL)


def delete(id):
    """
    Deletes a task from the json file
    :param id: indicates the task to delete
    :return: a list with all the task or an error if the task doesn't exist
    """
    data = jf.get_json()

    filtered_data = [item for item in data if item.get("id") != id]

    if len(data) == len(filtered_data):
        print(Fore.RED + f"Task {id} not found!" + Style.RESET_ALL)
    else:
        jf.set_json(filtered_data)
        print(Fore.GREEN + f"Task {id} deleted successfully!" + Style.RESET_ALL)
        list_tasks()


def update_status(status, id):
    """
    Updates the status of some task
    :param status: the new status of the task
    :param id: indicates the task to update
    :return: a list with all the task or an error if the task doesn't exist
    """
    data = jf.get_json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for task in data:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = now
            jf.set_json(data)
            print(Fore.GREEN + f"Task {task['id']} updated successfully!" + Style.RESET_ALL)
            list_tasks()
            return
    else:
        print(Fore.RED + f"Task {id} not found!" + Style.RESET_ALL)


def list_tasks(filter=False):
    """
    List all tasks in json file
    :param filter: opcional, to list only the task with some status
    :return: a list with all the task or an error if the task doesn't exist
    """
    data = jf.get_json()
    if filter:
        filtered_data = [task for task in data if task["status"] == filter]
        print(tabulate(filtered_data, headers="keys", tablefmt="fancy_grid"))

        if len(filtered_data) == 0:
            print(Fore.RED + f"No tasks with status {filter} found." + Style.RESET_ALL)
    else:
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


