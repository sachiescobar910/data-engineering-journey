# Reference: Loops (Week 1, Day 3-4)

**File:** `loops.py`
**Skills covered:** for loops, while loops, range(), break/continue

---

## for loops — repeat for each item in a sequence

```python
skills = ["Python", "SQL", "Airflow"]

for skill in skills:
    print(f"I need to learn {skill}")
```
`skill` is a variable name you choose — it holds one item at a time as the loop moves through the list. Use a **singular** name (`skill`) for the loop variable and a **plural** name (`skills`) for the full collection — makes the code much easier to read.

## range() — loop a specific number of times

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4  -- starts at 0, stops BEFORE 5

for i in range(1, 11):      # 1 to 10
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  -- step by 2
    print(i)
```

## while loops — repeat while a condition is True

```python
count = 0
while count < 5:
    print(count)
    count += 1   # same as count = count + 1
```
**Danger:** if you forget to update the variable controlling the condition, you get an **infinite loop**. Always make sure something inside the loop moves it toward becoming False.

## break and continue

```python
for i in range(10):
    if i == 5:
        break        # stops the loop completely
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue     # skips this one iteration, moves to the next
    print(i)         # only prints odd numbers
```

## enumerate() — get both the index and the item

```python
skills = ["Python", "SQL", "Airflow"]
for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")
# 1. Python
# 2. SQL
# 3. Airflow
```

---

## Common pitfalls (things I actually hit)

- **Using the same variable name for both the loop variable and the list** — e.g. `for skills in skills:` works, but it's confusing and bad practice. Use `skill` (singular) for one item, `skills` (plural) for the whole list.
- **Forgetting `+= 1`** inside a `while` loop — causes an infinite loop that never stops.
- `range(1, 7)` includes 1 but **stops before 7** — ends at 6, not 7. Easy to be off by one here.
