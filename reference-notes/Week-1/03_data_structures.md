# Reference: Lists, Tuples & Dictionaries (Week 1, Day 5-6)

**Files:** `List_and_tuples.py`, `data_structures.py`
**Skills covered:** lists, tuples, dictionaries, nested structures (list of dicts)

---

## Lists — ordered, changeable collections

```python
skills = ["Python", "SQL", "Airflow"]

skills[0]        # "Python"  -- indexing starts at 0
skills[-1]       # "Airflow" -- negative index counts from the end
skills[0:2]      # ["Python", "SQL"]  -- slicing (start:end, end excluded)

skills.append("Spark")       # adds to the end
skills.remove("SQL")         # removes by value
skills[0] = "Advanced Python"  # change an item by index
len(skills)                  # length of the list
```

## Tuples — ordered but UNCHANGEABLE

```python
coordinates = (25.2048, 55.2708)
# coordinates[0] = 10   # this would ERROR - tuples can't be modified
```
Used when data shouldn't change — fixed settings, or a pair of values returned together. Rarer than lists in everyday code, but you'll see them.

## Dictionaries — key-value pairs

The most important structure for data engineering — most real-world data (JSON, API responses, database rows) looks like this.

```python
employee = {
    "name": "Andres",
    "role": "Senior Biomedical Engineer",
    "years_experience": 6,
    "company": "ADSCC"
}

employee["name"]                      # "Andres" - access by key
employee["target_role"] = "Data Engineer"   # add a new key-value pair
employee["years_experience"] = 7            # update a value

for key, value in employee.items():
    print(f"{key}: {value}")
```
**Watch out:** `"years_of_experience": "6"` (with quotes) stores the number as text, not a number — it'll print fine but break if you try to do math with it later.

## Nesting — a list of dictionaries

```python
team = [
    {"name": "Andres", "role": "Data Engineer"},
    {"name": "Sara", "role": "Data Analyst"}
]

for person in team:
    print(f"{person['name']} is a {person['role']}")
```
**This exact pattern is extremely common.** When you load a CSV or JSON file into Python, this is essentially the shape the data takes — a list, where each item is a dictionary representing one row/record.

---

## Common pitfalls (things I actually hit)

- Storing a number as a string (`"6"` instead of `6`) in a dictionary — looks the same when printed, but breaks any math done on it later.
- Forgetting the quotes around dictionary **keys** (`name` vs `"name"`) — keys are text, so they need quotes just like any other string.
- Mixing up single vs. double access: `person['name']` inside an f-string needs single quotes if the outer string uses double quotes (or vice versa) — Python needs to tell them apart.
