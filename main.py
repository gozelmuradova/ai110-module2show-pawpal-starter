from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Gozel")

# Create pets
dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task1 = Task("Walk Buddy", datetime.now(), "daily")
task2 = Task("Feed Luna", datetime.now() + timedelta(hours=2), "daily")
task3 = Task("Vet visit", datetime.now() + timedelta(days=1), "once")

# Assign tasks
dog.add_task(task1)
cat.add_task(task2)
cat.add_task(task3)

# Scheduler
scheduler = Scheduler(owner)

# Print today's schedule
print("🐾 TODAY'S SCHEDULE:")
for task in scheduler.get_todays_tasks():
    print(f"- {task.description} at {task.time.strftime('%H:%M')}")