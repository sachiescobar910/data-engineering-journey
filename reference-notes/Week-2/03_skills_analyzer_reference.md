# Reference: Skills Analyzer (Week 2 Capstone)

**File:** `pandas_exercise.py`
**Skills covered:** functions, file handling, error handling, pandas (read/filter/transform/aggregate/write)

---

## Full code

```python
import pandas as pd

def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        return "Foundational"
    else:
        return "Advanced"

try:
    df = pd.read_csv("skills.csv")
except FileNotFoundError:
    print("skills.csv not found.")

df["difficulty"] = df["skill"].apply(classify_skill)
print(df)

advanced_skills = df[df["difficulty"] == "Advanced"]
print(advanced_skills)
print(df["difficulty"].value_counts())

df.to_csv("skills_analyzed.csv", index=False)
```

---

## Line-by-line breakdown

### `import pandas as pd`
Loads the pandas library and gives it the nickname `pd` — a universal convention, used in essentially every pandas file ever written. Must come before any pandas code runs.

### The function: `classify_skill`
```python
def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        return "Foundational"
    else:
        return "Advanced"
```
- `def` defines a reusable block of logic.
- `skill` is a **parameter** — a placeholder for whatever single value gets passed in when the function is called.
- The `if/else` checks the value and **returns** one of two text labels.
- `return` hands the value back to whoever called the function, and ends the function immediately — nothing is printed here, it's purely a calculation.
- **Key idea:** this function doesn't know or care about any list, loop, or DataFrame. It only knows how to judge one skill at a time. That's what makes it reusable in different contexts (a loop, a `.apply()`, a CSV writer — all three, in different exercises).

### Reading the file safely
```python
try:
    df = pd.read_csv("skills.csv")
except FileNotFoundError:
    print("skills.csv not found.")
```
- `try` tells Python: "attempt this code, but don't crash the whole program if it fails."
- `pd.read_csv("skills.csv")` reads the entire CSV file into a **DataFrame** — pandas' table-like structure, with rows and columns.
- `df` is the variable holding that table (short for "DataFrame" — also a convention).
- `except FileNotFoundError:` only runs if that *specific* error occurs — here, if `skills.csv` doesn't exist in the folder. Instead of a program-crashing red traceback, you get a friendly printed message and the program keeps running.
- **Important limitation to remember:** if the file genuinely isn't found, `df` never gets created, and every line below referencing `df` would then fail with a *different* error (`NameError`). In a more robust version, you'd want an `exit()` or a guard clause after the `except` block — something to explore later once we cover more advanced error handling.

### Adding a new column with `.apply()`
```python
df["difficulty"] = df["skill"].apply(classify_skill)
```
Read this in two halves:
- **Right side:** `df["skill"].apply(classify_skill)` — takes the `skill` column, and runs `classify_skill()` on **every single value in it**, one at a time, automatically. The result is a new column's worth of data (five `"Foundational"`/`"Advanced"` labels).
- **Left side:** `df["difficulty"] = ...` — stores that result as a column named `difficulty`. If the column already existed (it did, from an earlier exercise), this **overwrites** it with freshly calculated values. If it didn't exist, pandas would create it.
- This is the pandas equivalent of writing a `for` loop that calls `classify_skill()` on each item — just done internally, across the whole column, in one line.

### Filtering rows
```python
advanced_skills = df[df["difficulty"] == "Advanced"]
```
Two nested steps happening here:
1. **Inner part** — `df["difficulty"] == "Advanced"` checks every row's `difficulty` value and produces a column of `True`/`False` results.
2. **Outer part** — `df[ ... ]` uses those True/False values to keep only the rows marked `True`, discarding the rest.
- Plain English: *"Give me only the rows where difficulty equals Advanced."*
- Stored in a new variable, `advanced_skills`, so the original `df` is untouched.

### Counting values
```python
print(df["difficulty"].value_counts())
```
- `df["difficulty"]` selects the column.
- `.value_counts()` finds every **unique value** in that column (`"Advanced"`, `"Foundational"`) and counts how many rows have each one.
- Output is itself a small table: one row per unique value, with a count next to it. Extremely common in real data work — e.g. "how many orders per country," "how many users per plan."

### Saving the result
```python
df.to_csv("skills_analyzed.csv", index=False)
```
- `.to_csv(...)` writes the current state of `df` (which now includes the new `difficulty` column) out to a new file.
- `index=False` tells pandas **not** to include its internal row-numbering (0, 1, 2…) as an extra column in the saved file — without this, you'd get an unwanted unnamed column at the start of the CSV.

---

## The pattern underneath all of it

This script is a small but complete example of the **Extract → Transform → Load (ETL)** shape that almost every data pipeline follows:

| Step | What it means here | Line(s) |
|---|---|---|
| **Extract** | Read raw data from somewhere | `pd.read_csv("skills.csv")` |
| **Transform** | Apply logic to change/enrich the data | `classify_skill`, `.apply()`, filtering, `value_counts()` |
| **Load** | Save the final, transformed result somewhere new | `df.to_csv("skills_analyzed.csv", ...)` |

Every pipeline you build later — no matter how large or complex, what tools it uses, or what kind of data it handles — is fundamentally this same three-step shape.

---

## Common pitfalls to watch for (things I actually hit while building this)

- **Reading the same file twice** — once unprotected, once inside `try`. Only the `try` version should remain; delete any earlier unprotected read.
- **Indentation mismatches** between `if`/`else` — they must line up at the same level.
- **Forgetting `return`** inside a function — without it, the function runs but silently gives back nothing (`None`), which causes confusing errors later.
- **Confusing `return` with `print`** — `return` hands a value back for further use; `print` only displays it and discards it.
- **Typos in filenames** when switching between `.py` files and terminal commands — the editor and terminal are separate places with separate purposes.
