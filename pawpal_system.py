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
    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self, tasks):
        return sorted(tasks, key=lambda t: t.time)

    def detect_conflicts(self, tasks):
        warnings = []

        tasks_sorted = sorted(tasks, key=lambda t: t.time)

        for i in range(len(tasks_sorted) - 1):
            if tasks_sorted[i].time == tasks_sorted[i + 1].time:
                warnings.append(
                    f"Conflict: {tasks_sorted[i].description} and {tasks_sorted[i + 1].description}"
                )

        return warnings







from datetime import timedelta

def create_next_occurrence(task):
    if task.frequency == "daily":
        return Task(
            task.description,
            task.time + timedelta(days=1),
            "daily",
            False
        )

    if task.frequency == "weekly":
        return Task(
            task.description,
            task.time + timedelta(weeks=1),
            "weekly",
            False
        )

    return None