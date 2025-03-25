import functions
import argparse

parser = argparse.ArgumentParser(description="My Task Tracker task-cli")
# Commands
parser.add_argument("command", choices=["add", "update", "delete", "mark-in-progress", "mark-done", "list"])
# Dinamic args
parser.add_argument("task", type=str, nargs="*")

args = parser.parse_args()

print(args.command)
print(args.task)

if args.command == "add":
    functions.add()
elif args.command == "update":
    functions.update_task()
elif args.command == "delete":
    functions.delete()
elif args.command == "mark-in-progress":
    functions.update_status()
elif args.command == "mark-done":
    functions.update_status()
elif args.command == "list":
    functions.list()
