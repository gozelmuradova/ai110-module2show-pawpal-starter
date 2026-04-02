# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design had four main classes: Owner, Pet, Task, and Scheduler.

The Owner manages pets, the Pet stores info like name/type/age and its tasks, the Task represents things like feeding or walks with a due time and completion status, and the Scheduler handles all tasks in one place.

The main things the user can do are:
add/manage pets
schedule tasks
view daily tasks

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

At first, I was only keeping tasks inside each Pet, but I realized that would make it harder to see all tasks together.
So I added a Scheduler that manages all tasks globally. This made it easier to view things like “today’s tasks” across all pets.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler mainly focuses on time (due dates) and whether a task is completed or not.

I prioritized time because the whole point is to keep track of when pet care tasks need to be done.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff is that I didn’t include task priority, only time-based sorting.

I think this is fine because for a pet app, timing matters more, and adding priority would just make things more complicated for now.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help brainstorm the design, generate the UML diagram, and create class skeletons.

The most helpful prompts were specific ones like asking for a Mermaid diagram or Python dataclasses.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I didn’t always take AI suggestions directly. Sometimes it added extra complexity that wasn’t needed.

I just checked if it actually made sense for my app, and if not, I simplified it.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested things like adding pets, creating tasks, and getting tasks for today.

These are important because they’re basically the main features of the app.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I’m pretty confident it works for basic cases.

If I had more time, I’d test edge cases like empty task lists, duplicate times, or completed tasks showing up incorrectly.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I think my design structure came out really clean and easy to follow.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I’d probably add features like task priority or better filtering, and maybe improve how tasks are stored.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One big thing I learned is that designing first actually makes coding way easier, and AI helps a lot. butt you still have to think and not just accept everything.