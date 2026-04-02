from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime
import streamlit as st

# -----------------------------
# SESSION STATE (MUST BE FIRST)
# -----------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Gozel")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# -----------------------------
# UI SETUP
# -----------------------------
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown("Simple pet care scheduler demo built with Streamlit + OOP backend.")


# -----------------------------
# INPUTS
# -----------------------------
st.subheader("Add Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Create Pet"):
    new_pet = Pet(pet_name, species, age=0)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Pet '{pet_name}' added!")


st.divider()

st.subheader("Add Task")
task_title = st.text_input("Task title", value="Morning walk")
priority = st.selectbox("Priority", ["low", "medium", "high"])

if st.button("Add task"):

    # ensure pet exists
    if not st.session_state.owner.pets:
        st.error("Please create a pet first!")
    else:
        new_task = Task(
            description=task_title,
            time=datetime.now(),
            frequency="daily",
            completed=False
        )

        # attach to first pet
        st.session_state.owner.pets[0].add_task(new_task)

        # UI display list (optional but helpful)
        st.session_state.tasks.append({
            "title": task_title,
            "time": new_task.time.strftime("%H:%M"),
            "priority": priority
        })

        st.success("Task added!")


# -----------------------------
# DISPLAY PETS
# -----------------------------
st.divider()
st.subheader("🐾 Pets")

if st.session_state.owner.pets:
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets yet.")


# -----------------------------
# DISPLAY TASKS (UI TABLE)
# -----------------------------
st.subheader("📋 Tasks (UI View)")

if st.session_state.tasks:
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet.")

def mark_complete(self):
    self.completed = True


# -----------------------------
# SCHEDULE
# -----------------------------

st.divider()
st.subheader("📅 Generate Schedule")

if st.button("Generate schedule"):

    tasks = st.session_state.owner.get_all_tasks()

    if not tasks:
        st.warning("No tasks available.")
    else:
        st.subheader("Today's Schedule")

        for task in tasks:
            st.write(f"- {task.description} at {task.time.strftime('%H:%M')}")

def sort_by_time(self, tasks):
    return sorted(tasks, key=lambda task: task.time)


def filter_tasks_by_pet(self, owner, pet_name):
    tasks = owner.get_all_tasks()
    return [
        t for t in tasks
        if t in next(p for p in owner.pets if p.name == pet_name).tasks
    ]

def detect_conflicts(self, tasks):
    warnings = []

    sorted_tasks = sorted(tasks, key=lambda t: t.time)

    for i in range(len(sorted_tasks) - 1):
        current = sorted_tasks[i]
        next_task = sorted_tasks[i + 1]

        if current.time == next_task.time:
            warnings.append(
                f"⚠️ Conflict: '{current.description}' and '{next_task.description}' at {current.time.strftime('%H:%M')}"
            )

    return warnings


from datetime import timedelta

def create_next_occurrence(task):
    if task.frequency == "daily":
        return Task(
            description=task.description,
            time=task.time + timedelta(days=1),
            frequency="daily",
            completed=False
        )

    if task.frequency == "weekly":
        return Task(
            description=task.description,
            time=task.time + timedelta(weeks=1),
            frequency="weekly",
            completed=False
        )

    return None

def complete_task(self, task, pet):
    task.mark_complete()

    if task.frequency in ["daily", "weekly"]:
        new_task = create_next_occurrence(task)
        pet.add_task(new_task)

        