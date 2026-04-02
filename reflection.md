# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design had four main classes: Owner, Pet, Task, and Scheduler.

The Owner class manages all pets, the Pet class stores information like name, type, age, and its tasks. The Task class represents actions like feeding or walking with a due time and completion status, and the Scheduler handles organizing and managing tasks across pets.
At a high level, the main features I planned were:
adding and managing pets
scheduling tasks
viewing daily tasks

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed during implementation.

At first, I only stored tasks inside each Pet, but I realized that made it harder to view and manage all tasks together in one place. Because of that, I added a Scheduler class that can organize tasks globally.

This change made the system more flexible and allowed features like sorting tasks and detecting conflicts more easily.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler mainly considers time (task due time) and whether a task is completed.

I prioritized time because the main purpose of the app is to help users manage pet care routines and make sure tasks happen at the right time.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff I made was not including task priority levels (like high/medium/low).

I decided to keep it time-based only because it keeps the system simpler and easier to understand. For a pet care app, timing is the most important factor anyway, so adding priority felt unnecessary for this version.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI throughout the project for brainstorming the system design, generating initial class structures, and helping me debug errors when things didn’t work.

The most helpful prompts were the ones where I asked for specific implementation help, like building a Mermaid UML diagram or fixing Python class logic.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

There were times when I didn’t fully accept AI suggestions as is.

For example, AI sometimes suggested more complex solutions than needed, especially for sorting or scheduler logic. In those cases, I simplified the code because I wanted it to stay aligned with what we learned in class and be easier to debug.

I always checked whether the suggestion actually matched my design and only kept it if it made sense for my app.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested the core functionality of the app, including:
adding pets
creating tasks
sorting tasks
checking for task conflicts

These tests were important because they represent the main user features of the application.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I feel confident that the scheduler works correctly for normal use cases.

If I had more time, I would test edge cases like:
pets with no tasks
multiple tasks

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