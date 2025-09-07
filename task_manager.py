import json
import os
from datetime import date

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def get_tasks(self):
        return self.tasks

    def add_task(self, task_text, task_date=None):
        if task_date is None:
            task_date = str(date.today())
        self.tasks.append({"task": task_text, "date": task_date, "completed": False})
        self.save_tasks()

    def edit_task(self, index, new_text):
        self.tasks[index]["task"] = new_text
        self.save_tasks()

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    def toggle_task(self, index):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.save_tasks()






