# Reference: Functions & List Comprehensions (Week 1)

**Files:** `Functions.py`, `Functions_exercises.py`
**Skills covered:** function definitions, parameters, default values, return vs. print, scope, list comprehensions

---

## Functions — reusable blocks of code

```python
def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        difficulty = "Foundational"
    else:
        difficulty = "Advanced"
    return difficulty
```
- `def` starts the function definition.
- `skill` is a **parameter** — a placeholder for whatever value gets passed in when the function is called. Nothing runs when you just define a function; it's like writing a recipe card. It only runs when you *call* it.
- The colon `:` and indentation work exactly like `if`/`for` blocks.
- `return` hands a value back to whoever called the function, and **ends the function immediately** when it runs.

## Default parameter values

```python
def describe_skill(skill, level="Beginner"):
    return f"{skill} - {level}"

describe_skill("Python")                  # "Python - Beginner"  (uses the default)
describe_skill("SQL", "Intermediate")     # "SQL - Intermediate" (overrides the default)
```

## return vs. print — a critical distinction

```python
def add_print(a, b):
    print(a + b)      # shows the result on screen, but gives nothing back

def add_return(a, b):
    return a + b      # hands the result back so the caller can reuse it

total = add_return(2, 3) + 10   # works: 15
# add_print(2, 3) + 10          # would NOT work the same way - print() returns None
```
In real pipelines, functions almost always **return** values so the next step in the pipeline can use them, rather than just displaying them.

## Scope — variables inside a function are private

```python
def classify_skill(skill):
    difficulty = "Foundational"   # this 'difficulty' only exists INSIDE the function
    return difficulty

for skill in skills:
    difficulty = classify_skill(skill)   # this 'difficulty' is a DIFFERENT variable, living in the loop
    print(f"{skill} - {difficulty}")
```
The `skill` and `difficulty` inside the function and the `skill`/`difficulty` in the loop share names but are **completely separate variables**, living in separate "rooms." When the function finishes (after `return`), its internal variables disappear — only the returned value survives, passed out into the calling code.

This is a feature, not a bug: it means a function can be reused anywhere in a larger program without accidentally interfering with other code.

## List comprehensions — build a list in one line

```python
# The long way
squares = []
for n in range(1, 6):
    squares.append(n * n)

# The comprehension way
squares = [n * n for n in range(1, 6)]   # [1, 4, 9, 16, 25]
```

With a filter:
```python
skills = ["Python", "SQL", "Airflow", "Spark", "Docker"]
long_names = [s for s in skills if len(s) > 4]   # ["Python", "Airflow", "Spark", "Docker"]
```

**The general shape:**
```
[ what_to_keep   for item in collection   if condition ]
```
- `for s in skills` loops through the list, one item at a time, temporarily called `s`.
- `if len(s) > 4` is the filter — only items where this is True get included.
- `s` at the very start is "what to keep" — here, the item itself, unchanged.

This is identical logic to a regular `for` loop with an `if` and `.append()`, just compressed into one readable line once the pattern is familiar.

---

## Common pitfalls (things I actually hit)

- **Missing colon** after `def function_name(...)` — causes a `SyntaxError`.
- **Uneven indentation** between `if` and `else` inside a function — they must align.
- **Using `return` with no function to put it in**, or **using a variable (like `index`) inside a function that doesn't actually have access to it** — a function only knows about its own parameters and anything defined inside it, not variables from an outer loop.
- **Calling a function but not printing the result** — `result = my_function()` stores the value silently; you still need `print(result)` to see it.
- **Defining a function but never calling it** — nothing happens until it's actually called with `()`.
