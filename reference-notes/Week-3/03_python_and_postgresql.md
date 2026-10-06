# Reference: Connecting Python to PostgreSQL (Week 3)

**Files:** `db_connect.py`, `load_to_db.py`
**Skills covered:** psycopg2, connections and cursors, reading and writing from Python, parameterized queries, commit, idempotent loads, handling secrets

---

## Setup

```
pip install psycopg2-binary
```
`psycopg2` is the standard library that lets Python talk to PostgreSQL.

---

## Reading data from Python (`db_connect.py`)

```python
import psycopg2
from getpass import getpass

password = getpass("Enter your postgres password: ")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="data_engineering_practice",
    user="postgres",
    password=password
)

cur = conn.cursor()
cur.execute("SELECT * FROM skills;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
```

**The pieces:**
- **`psycopg2.connect(...)`** opens a connection to the database. The values are the same ones used to register the server in pgAdmin: host, port, database name, user, password.
- **`conn.cursor()`** creates a cursor, the object that sends SQL over the connection and holds the results. Think of the connection as the phone line and the cursor as the conversation on it.
- **`cur.execute("...")`** sends a SQL statement to PostgreSQL. It's the same SQL you would type in pgAdmin's Query Tool.
- **`cur.fetchall()`** returns all result rows as a list of tuples, e.g. `(16, 'Python', 'Foundational')`. (`fetchone()` returns just the next row.)
- **`cur.close()` / `conn.close()`** release the resources when you're done.

---

## Writing data from Python (`load_to_db.py`)

```python
import pandas as pd
import psycopg2
from getpass import getpass

password = getpass("Enter your postgres password: ")

conn = psycopg2.connect(
    host="localhost", port=5432,
    dbname="data_engineering_practice",
    user="postgres", password=password
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS skills_from_csv (
        id SERIAL PRIMARY KEY,
        skill_name VARCHAR(50),
        difficulty VARCHAR(20)
    );
""")

cur.execute("DELETE FROM skills_from_csv;")

df = pd.read_csv("skills_analyzed.csv")

for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO skills_from_csv (skill_name, difficulty) VALUES (%s, %s);",
        (row["skill"], row["difficulty"])
    )

conn.commit()

cur.execute("SELECT * FROM skills_from_csv;")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
```

### Parameterized queries (`%s`)

```python
cur.execute("INSERT INTO t (a, b) VALUES (%s, %s);", (value_a, value_b))
```
- The **SQL string** names the table and columns, with one `%s` placeholder per value.
- The **tuple** supplies the values, in the same order as the placeholders.
- **Never build SQL with f-strings** (`f"... VALUES ('{x}')"`). If a value contains something malicious, it can rewrite your SQL. That attack is called **SQL injection**. Placeholders make the database treat values purely as data.
- Column *names* in the table and in the DataFrame don't have to match (here `skill_name` vs. `skill`). What matters is the **order**: the first `%s` goes into the first column listed.

### `conn.commit()`
Changes made from Python (`INSERT`, `UPDATE`, `DELETE`, `CREATE`) sit in a pending **transaction** until you call `conn.commit()`. If the script ends without a commit, they are discarded. Reading data (`SELECT`) doesn't need a commit.

### Idempotent loads
A pipeline is **idempotent** if running it twice gives the same result as running it once. Here:
- `CREATE TABLE IF NOT EXISTS` doesn't fail if the table already exists.
- `DELETE FROM skills_from_csv;` clears old rows before loading, so re-running doesn't duplicate data.

Without these, every re-run would crash or double the data. Real pipelines get re-run after failures and on schedules, so this property matters a great deal. (In larger systems the usual approach is more refined than deleting everything, for example upserts, but the goal is the same.)

### Looping over a DataFrame
```python
for index, row in df.iterrows():
    ... row["column_name"] ...
```
`iterrows()` gives two values per pass: the row's index and the row itself, whose values you read by column name. Fine for small data. For large datasets, bulk-loading methods are far faster (a topic for later).

---

## Handling secrets: never hard-code passwords

A password typed into a `.py` file and pushed to a **public** GitHub repo is exposed to everyone, and bots scan GitHub for exactly this.
- `getpass()` asks for the password at runtime and hides what you type, so it never appears in the file.
- Later we'll use **environment variables** and a `.env` file listed in `.gitignore`, which is the standard approach for pipelines that run unattended.
- If a password ever *does* get committed, changing it is the fix. Deleting it from the file doesn't help, because it remains in the Git history.

---

## Common pitfalls (things I actually hit)

- **`password authentication failed for user "postgres"`**: the connection itself worked (the server was reached), but the password was wrong. `getpass` hides input, so typos are easy to miss. Fix: retype carefully, or reset it from pgAdmin with `ALTER USER postgres PASSWORD 'new_password';`. Resetting the password does not affect any data.
- **Putting `row[...]` values inside the SQL string** instead of the tuple, and leaving `...` placeholders unfilled. The SQL string holds table/column names and `%s` slots; the tuple holds the values.
- **Double quotes inside a double-quoted string** (`"... row["skill"] ..."`) end the string early and cause a `SyntaxError`.
- **Forgetting `conn.commit()`**: the script runs without errors, but nothing is saved.
- **Auto-increment ids keep climbing** across re-runs (ids 1-5, then 6-10). This is expected, since `SERIAL` never reuses numbers.
