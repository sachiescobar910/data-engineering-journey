# Reference: JOINs & Aggregation (Week 3)

**Tables used:** `skills`, `learning_log`
**Skills covered:** foreign keys, JOIN, GROUP BY, aggregate functions (SUM)

---

## Setting up a second, related table

```sql
CREATE TABLE learning_log (
    id SERIAL PRIMARY KEY,
    skill_id INTEGER REFERENCES skills(id),
    hours_studied INTEGER,
    week_number INTEGER
);
```
- `skill_id INTEGER REFERENCES skills(id)` is a **foreign key**: a column whose values must correspond to an existing `id` in the `skills` table.
- This is literally how two tables become *related* in a relational database — one table stores a pointer to a row in another table, rather than duplicating that row's data.

```sql
INSERT INTO learning_log (skill_id, hours_studied, week_number) VALUES
(16, 10, 1),
(17, 8, 1),
(18, 5, 3),
(19, 4, 3),
(20, 3, 3);
```
Each `skill_id` here corresponds to a real `id` already present in the `skills` table (confirmed first with `SELECT * FROM skills;` before inserting).

---

## JOIN — combining two tables

```sql
SELECT skills.skill_name, skills.difficulty, learning_log.hours_studied, learning_log.week_number
FROM skills
JOIN learning_log ON skills.id = learning_log.skill_id;
```

**How to read this:**
- `FROM skills` — start with the `skills` table.
- `JOIN learning_log` — bring in the `learning_log` table too.
- `ON skills.id = learning_log.skill_id` — the matching rule. PostgreSQL pairs up rows from each table wherever this condition is true.
- `SELECT skills.skill_name, ...` — because columns are being pulled from two different tables at once, each column is prefixed with its table name, to avoid any ambiguity about where it's coming from.

**Key insight:** the match is based on **values, not row position or order**. A row in `learning_log` doesn't need to be inserted in any particular order, and the two tables don't need the same number of rows — PostgreSQL simply looks for rows where `skills.id` and `learning_log.skill_id` hold the same number, wherever each one happens to sit in its table.

**Result shape:** one unified table combining columns from both sources — e.g., "Python — Foundational — 10 hours — Week 1" — without duplicating the skill's details across every log entry.

---

## GROUP BY — aggregating data

```sql
SELECT skills.difficulty, SUM(learning_log.hours_studied) AS total_hours
FROM skills
JOIN learning_log ON skills.id = learning_log.skill_id
GROUP BY skills.difficulty;
```

- `SUM(learning_log.hours_studied)` adds up the `hours_studied` values.
- `AS total_hours` renames the result column for readability (an **alias**).
- `GROUP BY skills.difficulty` collapses the result from one row per skill into one row per **unique difficulty value**, applying the `SUM()` within each group.

**Result:**
```
difficulty     total_hours
Foundational   18
Advanced       12
```

**Other common aggregate functions**, usable the same way as `SUM()`:
- `COUNT(*)` — number of rows in each group
- `AVG(column)` — average value
- `MIN(column)` / `MAX(column)` — smallest/largest value

**The general pattern to remember:**
```
SELECT <grouping column>, <aggregate_function(column)>
FROM <table(s)>
[JOIN ...]
GROUP BY <grouping column>;
```
This combination — join related tables, then group and aggregate — is one of the most common query shapes in real data engineering and analytics work. "Total sales per region," "average session length per user type," "count of orders per status" are all this exact pattern, just with different tables and columns.

---

## Common pitfalls (things I actually hit)

- **Forgetting to prefix column names with their table** (`skill_name` vs. `skills.skill_name`) once two tables are involved — can cause ambiguity errors if both tables happen to share a column name.
- **Using the wrong IDs when inserting related data** — easy to assume IDs start at 1, but auto-incrementing counters (`SERIAL`) keep climbing even after rows are deleted. Always confirm actual IDs with a `SELECT` before inserting related data elsewhere.
- **Trying to SELECT a column that isn't in the GROUP BY and isn't wrapped in an aggregate function** — PostgreSQL will reject this, since it wouldn't know which value to show for that column within a collapsed group.
