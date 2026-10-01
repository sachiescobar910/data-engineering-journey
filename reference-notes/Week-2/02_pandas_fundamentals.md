# Reference: Pandas Fundamentals (Week 2)

**File:** `pandas_intro.py`
**Skills covered:** DataFrames, reading CSVs, inspecting data, filtering, adding columns, sorting, aggregating

---

## What pandas is for

Pandas is built around one core object: the **DataFrame** — a table living inside Python, with rows and columns, like a spreadsheet. It lets you do in one line what previously took a `for` loop and several lines of manual `csv` module code.

## Reading a CSV

```python
import pandas as pd   # 'pd' is the near-universal convention for importing pandas

df = pd.read_csv("skills.csv")
print(df)
```
One line loads the entire file into a DataFrame, complete with an automatic index column (0, 1, 2…) on the left.

## Inspecting a DataFrame

```python
df.head()          # first 5 rows (useful for peeking at huge datasets)
df.shape            # (rows, columns) as a tuple, e.g. (5, 2)
df.columns          # the column names
```

## Selecting a column

```python
df["skill"]
```
Square-bracket syntax here works a lot like accessing a dictionary value by key — not a coincidence, pandas columns behave similarly.

## Filtering rows

```python
df[df["difficulty"] == "Advanced"]
```
This looks confusing at first because of the nested brackets — break it into two steps:
1. **Inner part:** `df["difficulty"] == "Advanced"` checks *every row* in that column and produces a column of `True`/`False` values.
2. **Outer part:** `df[ ... ]` uses those True/False values to keep only the rows marked `True`.

Plain English: *"Give me only the rows where difficulty equals Advanced."* This does the same job as a `for` loop with an `if` check inside it — pandas just does it across the whole table at once, internally.

## Adding a new column

```python
df["skill_length"] = df["skill"].apply(len)
```
- `df["skill"].apply(len)` runs the `len()` function on **every value** in the `skill` column, all at once.
- `.apply()` isn't limited to built-in functions — you can pass it your own custom functions too:

```python
df["difficulty"] = df["skill"].apply(classify_skill)
```
This runs your own `classify_skill` function on every row's skill value, and stores the results as a new (or overwritten) column.

## Working with text columns directly

```python
df["first_letter"] = df["skill"].str[0]
```
The `.str` accessor lets you apply string operations (slicing, in this case) across an entire column at once, without writing a loop.

## Sorting

```python
df_sorted = df.sort_values("skill_length", ascending=False)
```
Sorts the whole table by a given column. `ascending=False` sorts largest to smallest. Note: sorting **reorders rows but keeps their original index numbers** — so after sorting, the index column on the left may look "out of order" (e.g. 2, 0, 4, 3, 1) even though the rows themselves are correctly sorted.

## Counting unique values

```python
df["difficulty"].value_counts()
```
Finds every **unique value** in a column and counts how many rows have each one. Equivalent to manually looping and tallying occurrences, but in one line. Very commonly used in real data work (e.g. "how many orders per country").

## Saving a DataFrame back to a file

```python
df.to_csv("skills_analyzed.csv", index=False)
```
`index=False` prevents pandas from adding its internal row-numbering as an extra, unwanted column in the saved file.

---

## Common pitfalls (things I actually hit)

- **Installing pandas into the wrong Python environment** — if you have multiple Python installations (e.g. a plain one from python.org *and* Anaconda), `pip install pandas` might succeed in one but VS Code could be pointed at a different one that doesn't have it. Fix: `Ctrl+Shift+P` → "Python: Select Interpreter" → choose the one that has pandas installed (check with `python -c "import pandas; print(pandas.__version__)"` in a fresh terminal).
- **A stray, incomplete `.venv` folder** can appear and cause confusing errors if VS Code tries to use it before it's properly set up — safe to ignore or delete if you're not intentionally using virtual environments yet.
- **Confusing `df["col"] = value` (assignment) with `df["col"] == value` (comparison)** — single `=` sets a column's values; double `==` checks equality and produces True/False.
