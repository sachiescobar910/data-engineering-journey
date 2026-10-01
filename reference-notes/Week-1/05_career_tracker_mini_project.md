# Reference: Career Transition Tracker (Week 1, Day 7 Mini Project)

**File:** `career_tracker.py`
**Skills covered:** combining variables, dictionaries, loops, enumerate(), conditional logic, and f-strings into one program

---

## Full code

```python
profile = {
    "name": "Andres",
    "target_role": "Data Engineer"
}

skills = ["Python", "SQL", "Airflow", "Spark", "Docker"]

for index, skill in enumerate(skills, start=1):
    if skill == "Python" or skill == "SQL":
        difficulty = "Foundational"
    else:
        difficulty = "Advanced"
    print(f"{index}. {skill} - {difficulty}")

print(f"{profile['name']} needs to learn {len(skills)} skills to become a {profile['target_role']}, starting from Foundational to Advanced topics.")
```

---

## What this project demonstrates

This was the first time multiple separate concepts were combined into **one coherent program**, rather than practiced in isolation. That combination is the real skill — individual pieces (a loop, a dictionary, an if/else) are easy on their own; knowing how to weave them together to solve an actual problem is what the job looks like day to day.

## Line-by-line breakdown

### The profile dictionary
```python
profile = {
    "name": "Andres",
    "target_role": "Data Engineer"
}
```
Stores identity-level info that doesn't change during the loop — accessed later with `profile['name']` and `profile['target_role']`.

### The loop with enumerate()
```python
for index, skill in enumerate(skills, start=1):
```
- `enumerate()` gives you **two** values per loop pass: a running count (`index`) and the item itself (`skill`).
- `start=1` makes the counting begin at 1 instead of Python's default of 0 — so the output reads "1. Python" instead of "0. Python," which is more natural for a numbered list shown to a person.

### The conditional logic inside the loop
```python
if skill == "Python" or skill == "SQL":
    difficulty = "Foundational"
else:
    difficulty = "Advanced"
```
Same classification logic used elsewhere, but this time it's written directly inside the loop (rather than packaged into a separate function, which came in the *next* exercise, `Functions_exercises.py`). Comparing these two versions side-by-side is a good way to see exactly what moving logic into a function buys you: reusability, and a loop body that's easier to read because the decision-making is tucked away elsewhere.

### Dynamic values instead of hardcoded ones
```python
print(f"... needs to learn {len(skills)} skills ...")
```
`len(skills)` calculates the count directly from the list, instead of typing the number `5` by hand. If a 6th skill were added to the list later, this line would update automatically — no need to hunt down and edit a hardcoded number. **General habit worth keeping: calculate values from data wherever possible, rather than typing them in literally.**

---

## Common pitfalls (things I actually hit)

- Using the **same variable name** for the list and the loop variable (`for skills in skills:`) — confusing, even though Python allows it. Fixed by using `skill` (singular) for the loop variable.
- Leaving **old/superseded code** at the top of the file from earlier attempts — not an error, but worth cleaning up once a better version exists further down. Real projects get refactored like this constantly as understanding improves.
