from pawpal_system import Pet, Task
from datetime import datetime


def test_task_completion():
    task = Task("Test task", datetime.now(), "daily")
    task.mark_complete()
    assert task.completed == True


def test_task_addition():
    pet = Pet("Buddy", "Dog")
    task = Task("Walk", datetime.now(), "daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1