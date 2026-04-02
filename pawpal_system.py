from dataclasses import dataclass
from typing import List
from datetime import datetime


# ---------------- TASK ----------------
@dataclass
class Task:
    description: str
    time: datetime
    frequency: str
    completed: bool = False
    pet_id: int = None

    def mark_complete(self):
        self.completed = True


# ---------------- PET ----------------
class Pet:
    def __init__(self, name: str, species: str, age: int = 0, tasks: List[Task] = None):
        self.name = name
        self.species = species
        self.age = age
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


# ---------------- OWNER ----------------
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


# ---------------- SCHEDULER ----------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_tasks(self):
        today = datetime.now().date()
        return [
            task for task in self.owner.get_all_tasks()
            if task.time.date() == today
        ]