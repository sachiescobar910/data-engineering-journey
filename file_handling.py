with open("skills.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("skills_backup.txt", "w") as backup_file:
    with open("skills.txt", "r") as file:
        for line in file:
            backup_file.write(line)

try:
    with open("does_not_exist.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file you are trying to open doesn't exist.")

import csv

def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        difficulty = "Foundational"
    else:
        difficulty = "Advanced"
    return difficulty

skills = ["Python", "SQL", "Airflow", "Spark", "Docker"]

with open("skills.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["skill", "difficulty"])                        # header row
    for skill in skills:
        difficulty = classify_skill(skill)
        writer.writerow([skill, difficulty])



