from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    due_time: datetime
    completed: bool
    pet_id: int

    def mark_complete(self):
        pass


@dataclass
class Pet:
    id: int
    name: str
    species: str
    age: int
    tasks: List[Task]

    def add_task(self, task: Task):
        pass

    def remove_task(self, task_id: int):
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet_id: int):
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        pass

    def remove_task(self, task_id: int):
        pass

    def get_tasks_for_today(self) -> List[Task]:
        pass

    def get_upcoming_tasks(self) -> List[Task]:
        pass