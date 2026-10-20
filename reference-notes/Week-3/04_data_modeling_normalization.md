# Reference: Data Modeling & Normalization (Week 3)

**Tables used:** `patients`, `visits` (fake data only), plus `skills` and `learning_log` from earlier
**Skills covered:** normalization, one-to-many relationships, foreign keys, referential integrity, JOIN and GROUP BY with COUNT

---

## Why data is split across tables

Imagine storing everything in one table:

```
skill_name | difficulty   | hours_studied | week_number
Python     | Foundational | 6             | 1
Python     | Foundational | 4             | 2
SQL        | Foundational | 8             | 1
```

Problems with this design:
- **Redundancy:** "Python" and "Foundational" are repeated on every study session.
- **Update problem:** reclassifying Python means editing every Python row. Missing one leaves the data contradicting itself.
- **Deletion problem:** deleting the last study session for a skill erases the skill from the data entirely.

**Normalization** fixes this by storing each fact **once**. Skill details live in `skills`, study sessions live in `learning_log`, and a foreign key links them. Reclassifying Python then means changing one row in one place.

## Key terms

- **Primary key:** a column (usually `id SERIAL PRIMARY KEY`) that uniquely identifies each row in its own table.
- **Foreign key:** a column that points to a primary key in another table, declared with `REFERENCES other_table(id)`.
- **One-to-many relationship:** one row in table A relates to many rows in table B, but each row in B belongs to exactly one row in A. Examples: one skill has many study sessions; one patient has many visits. This is the most common relationship in databases.
- **Referential integrity:** the database's guarantee that every foreign key points to a row that really exists.

---

## The healthcare example (fake data only)

```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    birth_year INTEGER
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(id),
    visit_date DATE,
    department VARCHAR(50)
);
```

- **Create the parent table first.** `visits` points at `patients`, so `patients` must already exist, or PostgreSQL rejects the reference.
- `DATE` is the data type for calendar dates, written in quotes as `'2026-01-10'` (year-month-day).
- Patient details are stored once in `patients`; each visit stores only a `patient_id` pointing back.

> Real patient data is protected by privacy regulations and needs careful handling (access control, anonymization, compliance rules). Practice projects should always use fake or properly de-identified data.

## JOIN: each visit with the patient's name

```sql
SELECT patients.full_name, patients.birth_year, visits.patient_id, visits.visit_date, visits.department
FROM patients
JOIN visits ON patients.id = visits.patient_id;
```
Returns one row per visit. The `ON` clause is always `table_a.primary_key = table_b.foreign_key`, written as `table.column`.

## GROUP BY with COUNT: visits per patient

```sql
SELECT patients.full_name, COUNT(*) AS total_visits
FROM patients
JOIN visits ON patients.id = visits.patient_id
GROUP BY patients.id
ORDER BY patients.full_name;
```
- `COUNT(*)` counts the rows in each group (compare `SUM(column)`, which adds up values).
- Group by the **primary key** (`patients.id`), not by name, because two different patients could share a name and be wrongly merged into one row.
- `ORDER BY` goes last, because `GROUP BY` does not guarantee any particular row order.

Result: Patient A: 2, Patient B: 1, Patient C: 3.

---

## Referential integrity in action

```sql
INSERT INTO visits (patient_id, visit_date, department)
VALUES (99, '2026-05-01', 'Cardiology');
```
No patient 99 exists, so PostgreSQL rejects it:
```
ERROR: insert or update on table "visits" violates foreign key constraint "visits_patient_id_fkey"
Key (patient_id)=(99) is not present in table "patients".
```
- `visits_patient_id_fkey` is the auto-generated constraint name (table, column, `fkey`).
- Nothing is saved when an insert fails, but the `SERIAL` counter may still advance, so ids can skip numbers.
- A CSV file or DataFrame would have accepted this row. The database enforces consistency for every program that writes to it.

---

## Common pitfalls (things I actually hit)

- **Forgetting `REFERENCES` on the foreign key column.** Without it, `patient_id` is a plain number column with no link and no protection against bad values.
- **Leaving out a data type** for a column, or forgetting a comma between column definitions, causes a syntax error.
- **Merging table and column names** (`patients_id`, `patients.patients.id`). The form is `table.column`: one table name, one dot, one column name.
- **A semicolon in the middle of a query.** `;` ends the statement, so any `GROUP BY` or `ORDER BY` on the next line is read as a separate, invalid statement. Only the last line gets the semicolon.
- **Grouping by a name instead of the primary key**, which can silently merge different people who share a name.
