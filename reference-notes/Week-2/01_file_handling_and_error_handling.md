# Reference: File Handling & Error Handling (Week 2)

**Files:** `reading_files.py`, `file_handling.py`
**Skills covered:** reading/writing text files, the `with` statement, reading/writing CSVs, try/except

---

## Reading files

```python
file = open("data.txt", "r")   # "r" = read mode
content = file.read()
print(content)
file.close()   # must remember to close it manually
```

The problem with this approach: if an error happens between `open()` and `close()`, the file might never get closed properly. The standard, safer pattern:

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here, even if something inside goes wrong
```
`with` handles opening and closing for you — this is how virtually all real Python code opens files.

## Reading line by line

```python
with open("skills.txt", "r") as file:
    for line in file:
        print(line.strip())
```
`.strip()` removes the extra newline character (`\n`) that comes along with each line when read from a file — without it, you'd get unwanted blank lines in your output.

## Writing files

```python
with open("output.txt", "w") as file:   # "w" = write mode, OVERWRITES the whole file
    file.write("Hello from Python\n")
    file.write("Second line\n")
```
- `"w"` mode wipes the file clean first if it already exists — be careful with this.
- `"a"` mode (append) adds to the end instead of overwriting, if you need that behavior instead.

## Copying/transforming data from one file to another

```python
with open("skills_backup.txt", "w") as backup_file:
    with open("skills.txt", "r") as file:
        for line in file:
            backup_file.write(line)
```
Two files open at once — one for reading, one for writing — copying each line across. **This "read from one place, write to another" pattern is the core of almost every ETL pipeline, just scaled up to much bigger datasets later.**

## Working with CSV files

Reading:
```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)   # each row comes back as a list, e.g. ['Andres', '33', 'Data Engineer']
```

Writing:
```python
import csv

with open("skills.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["skill", "difficulty"])         # header row
    for skill in skills:
        difficulty = classify_skill(skill)
        writer.writerow([skill, difficulty])         # one data row per skill
```
- `csv.writer(file)` creates a **writer object** that knows how to correctly format data as CSV (commas, line breaks, etc.) and attaches to the open file.
- `writer.writerow([...])` takes a list and writes it as one line, with items separated by commas.
- `newline=""` is a Windows-specific quirk — without it, CSV writing can insert unwanted extra blank lines. Just include it by convention whenever writing CSVs.

## Error handling — try/except

```python
try:
    with open("does_not_exist.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("That file doesn't exist.")
```
- Python attempts the code inside `try`.
- If the **specific** error named in `except` happens, Python jumps into that block instead of crashing the whole program.
- You can catch multiple error types separately:

```python
try:
    number = int("abc")
except ValueError:
    print("That wasn't a valid number.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Something else went wrong: {e}")   # catches anything not caught above
```

---

## Common pitfalls (things I actually hit)

- **Reading the same file twice** — once unprotected outside `try`, once safely inside it. If an unprotected read exists earlier in the file, it defeats the whole purpose of the `try/except` below it. Only one version should remain.
- **`import csv` placed in the middle of the file** instead of at the very top — works, but it's Python convention to put all imports first, before any other code.
- **Forgetting `newline=""`** when writing CSVs on Windows — can introduce extra blank lines in the output file.
- **Using `"w"` mode when you meant `"a"`** (append) — accidentally wiping out existing file content instead of adding to it.
