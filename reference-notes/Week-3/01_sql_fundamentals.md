# Reference: SQL Fundamentals & PostgreSQL Setup (Week 3)

**Tool:** pgAdmin 4, connected to a local PostgreSQL server
**Database:** `data_engineering_practice`
**Skills covered:** CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY, comments

---

## The setup

- **PostgreSQL** is the actual database engine — the program that stores and manages your data, running quietly in the background as a service on your computer.
- **pgAdmin** is a visual tool for *looking at and controlling* PostgreSQL — it doesn't store data itself, it just gives you a friendly interface (the Query Tool, table browsers, etc.) to talk to the database.
- A **server** (e.g. "Local PostgreSQL") is one running instance of PostgreSQL you've connected to.
- A **database** (e.g. `data_engineering_practice`) lives inside a server, and holds your tables. One server can host many separate databases.

## Creating a table

```sql
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    skill_name VARCHAR(50),
    difficulty VARCHAR(20)
);
```
- `CREATE TABLE skills (...)` defines a new table and its columns, all in one statement.
- `id SERIAL PRIMARY KEY` — a unique, auto-incrementing whole number for each row (1, 2, 3…). `PRIMARY KEY` marks it as the unique identifier for each record — no two rows can share the same `id`.
- `VARCHAR(50)` — a text column with a maximum length (here, 50 characters). Choosing a sensible max length is part of designing a table properly.
- **Running `CREATE TABLE` again for a table that already exists causes an error** (`relation "skills" already exists") — comment it out once it's successfully run, rather than leaving it active.

## Inserting data

```sql
INSERT INTO skills (skill_name, difficulty) VALUES
('Python', 'Foundational'),
('SQL', 'Foundational'),
('Airflow', 'Advanced'),
('Spark', 'Advanced'),
('Docker', 'Advanced');
```
- Lists which columns you're filling in (`skill_name`, `difficulty`) — `id` is left out because PostgreSQL fills it automatically (`SERIAL`).
- One set of parentheses per row being inserted, separated by commas, ending in a semicolon.
- **Running this twice inserts duplicate data** — PostgreSQL doesn't stop you from inserting the same values again unless you explicitly set up a rule against it (a topic for later — unique constraints).

## Reading data: SELECT

```sql
SELECT * FROM skills;
```
- `SELECT *` means "give me every column."
- `FROM skills` specifies which table.
- This is the single most common SQL statement you will ever write.

Selecting specific columns instead of everything:
```sql
SELECT skill_name FROM skills;
```

## Filtering: WHERE

```sql
SELECT * FROM skills WHERE difficulty = 'Advanced';
```
Only returns rows where the condition is true — the SQL equivalent of pandas' `df[df["difficulty"] == "Advanced"]`. Same underlying idea, different syntax.

## Sorting: ORDER BY

```sql
SELECT * FROM skills ORDER BY skill_name ASC;
```
- `ASC` = ascending (A→Z, smallest→largest). `DESC` = descending (Z→A, largest→smallest).
- Sorting doesn't change the data itself — it only changes the order the results are displayed in.

## Combining everything

```sql
SELECT skill_name FROM skills WHERE difficulty = 'Foundational' ORDER BY skill_name;
```
Pick specific column(s), filter rows, sort the result — all in one readable statement. This is the shape most real-world queries take.

## Deleting data

```sql
DELETE FROM skills;
```
Removes **all rows** from the table, but the table structure itself remains. Can also be filtered: `DELETE FROM skills WHERE difficulty = 'Advanced';` would only delete matching rows.

## Comments — disabling code without deleting it

```sql
-- this whole line is ignored
SELECT * FROM skills;  -- this part is ignored, the SELECT still runs

/*
This entire
block is ignored
*/
```
In pgAdmin, select a line and press **Ctrl + /** to toggle a comment on/off quickly.

---

## Running queries in pgAdmin — an important gotcha

**F5 (or the Play button) runs the ENTIRE contents of the query editor, top to bottom — not just the line your cursor is on.** This caused real duplicate data during practice: an old `INSERT` statement left active in the editor ran again every time a *different* new statement below it was executed.

**To run only a specific statement:** highlight/select just that text with your mouse first, then press F5. Only the highlighted portion runs.

**Best practice going forward:** comment out (`--`) any statement once you're done with it (like `CREATE TABLE` after the table exists, or an `INSERT` after the data is in), so re-running the whole file doesn't repeat actions that should only happen once.

---

## Common pitfalls (things I actually hit)

- **Running the whole editor instead of one statement** — caused a table-already-exists error and, separately, duplicated data (15 rows instead of 5) from repeated `INSERT`s.
- **Auto-increment IDs don't reset after a DELETE** — if you delete all rows and re-insert, new rows continue numbering from where the counter left off (e.g. starting at 16, not 1). This is expected PostgreSQL behavior, not a bug.
- **Mixing up Data Output vs. Messages tabs** — actual query *results* (rows of data) appear in **Data Output**; status info like "Query returned successfully" or row counts appears in **Messages**.
- **A fresh, unconfigured `.venv` or missing server registration** — occasionally pgAdmin doesn't auto-register the local server after install; it can be added manually via "Add New Server" using `localhost`, port `5432`, and the postgres password set during installation.
