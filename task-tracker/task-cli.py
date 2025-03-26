"""
CLI controller
"""

import functions
import argparse

parser = argparse.ArgumentParser(description="My Task Tracker task-cli")
parser.add_argument("command", choices=["add", "update", "delete", "mark-in-progress", "mark-done", "list"])
parser.add_argument("task", type=str, nargs="*")

args = parser.parse_args()

desc = args.task
com = args.command

if com == "add":
    functions.add(desc[0])
elif com == "update":
    id = int(desc[0])
    functions.update_task(id, desc[1])
elif com == "delete":
    id = int(desc[0])
    functions.delete(id)
elif com == "mark-in-progress" or com == "mark-done":
    status = com.lstrip("mark-")
    id = int(desc[0])
    functions.update_status(status, id)
elif com == "list":
    if desc:
        status = desc[0]
        functions.list_tasks(status)
    else:
        functions.list_tasks()
