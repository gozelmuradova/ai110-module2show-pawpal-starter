from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, timedelta


def test_task_sorting():
    owner = Owner("Test")
    pet = Pet("Mochi", "dog", 2)
    owner.add_pet(pet)

    t1 = Task("Later task", datetime.now() + timedelta(hours=2), "daily", False)
    t2 = Task("Earlier task", datetime.now(), "daily", False)

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time(pet.tasks)

    assert sorted_tasks[0].description == "Earlier task"


def test_task_attachment():
    owner = Owner("Test")
    pet = Pet("Mochi", "dog", 2)
    owner.add_pet(pet)

    task = Task("Feed", datetime.now(), "daily", False)
    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_conflict_detection():
    owner = Owner("Test")
    pet = Pet("Mochi", "dog", 2)
    owner.add_pet(pet)

    time = datetime.now()

    t1 = Task("Walk", time, "daily", False)
    t2 = Task("Feed", time, "daily", False)

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)
    warnings = scheduler.detect_conflicts(pet.tasks)

    assert len(warnings) > 0


def test_empty_tasks():
    owner = Owner("Test")
    pet = Pet("Mochi", "dog", 2)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    assert scheduler.sort_by_time(pet.tasks) == []


def test_recurring_task_logic():
    task = Task("Walk", datetime.now(), "daily", False)

    task.mark_complete()

    from pawpal_system import create_next_occurrence
    new_task = create_next_occurrence(task)

    assert new_task is not None
    assert new_task.description == "Walk"