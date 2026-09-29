# Reading files
file = open("data.txt", "r")   # "r" means read mode
content = file.read()
print(content)
file.close()   # always close what you open

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here, even if something goes wrong inside, most used code for working with files

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())   # .strip() removes the extra newline character

# Writing files
with open("output.txt", "w") as file:   # "w" means write mode (overwrites!)
    file.write("Hello from Python\n")
    file.write("Second line\n")
# "w" mode overwrites the whole file if it already exists. If you want to add to the end instead of replacing it, use "a" (append mode).

# Working with CSV files
# Read he file
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)   # each row comes back as a list, e.g. ['Andres', '33', 'Data Engineer']

# Write a CSV file
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "role"])       # header row
    writer.writerow(["Andres", "Data Engineer"])

# Error handling — try/except
try:
    with open("does_not_exist.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("That file doesn't exist.")

try:
    number = int("abc")   # this will fail - "abc" isn't a number
except ValueError:
    print("That wasn't a valid number.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Something else went wrong: {e}")   # catches anything not caught above