# Reference: Variables, Data Types & Control Flow (Week 1, Day 1-2)

**Files:** `variables.py`, `control_flow.py`
**Skills covered:** variables, data types, f-strings, comparison operators, if/elif/else, logical operators

---

## Variables

```python
name = "Andres"
age = 33
```
A variable is a labeled box that stores a value. Python figures out the type automatically — no need to declare it yourself.

## Core data types

```python
name = "Andres"        # str (text) - always in quotes
age = 33                # int (whole number)
height = 1.75           # float (decimal number)
is_engineer = True      # bool (True or False)
```
**Watch out:** `"6"` (string) and `6` (int) look similar but behave very differently. You can't do math on a string version of a number without converting it first.

## f-strings — combining text and variables

```python
current_job = "Senior Biomedical Engineer"
years_of_experience = 6

print(f"{name} has worked as a {current_job} for {years_of_experience} years.")
```
- The `f` right before the opening quote turns on f-string mode.
- Anything inside `{ }` gets evaluated and inserted directly into the string — no messy `+` concatenation needed, and numbers get converted to text automatically.

## Operators

```python
# Arithmetic
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 / 3   # 3.333... (always returns a float)
10 // 3  # 3  (floor division - drops the decimal)
10 % 3   # 1  (modulo - the remainder)

# Comparison (always returns True or False)
10 > 3    # True
10 == 3   # False  -- == checks equality; = assigns a value. Easy to mix up!
```

## if / elif / else

```python
years_of_experience = 6

if years_of_experience < 2:
    print("Junior level")
elif years_of_experience < 5:
    print("Mid level")
elif years_of_experience < 10:
    print("Senior level")
else:
    print("Expert level")
```
- The colon `:` at the end of `if`/`elif`/`else` is required.
- **Indentation is not just style** — it's how Python knows what code belongs inside each block.
- Python checks conditions top to bottom and runs the **first one that's True**, then skips the rest, even if a later condition would also be True.

## Logical operators

```python
age = 33
years_of_experience = 6

if age > 25 and years_of_experience > 5:
    print("Experienced professional")   # BOTH must be True

if years_of_experience < 2 or age < 22:
    print("Early career")               # at least ONE must be True
```

---

## Common pitfalls (things I actually hit)

- **Editor vs. terminal confusion** — typing a command like `python variables.py` *inside* the code file itself causes a `SyntaxError`, because Python tries to run it as code. Commands go in the terminal; code goes in the editor.
- **Mismatched indentation** between `if`/`elif`/`else` blocks causes errors — they all need to line up at the same level.
- **Using `=` instead of `==`** inside a condition — `=` assigns, `==` compares.
