def calculate_years_remaining(current_years, target_years):
    return target_years - current_years

result = calculate_years_remaining(6, 10)
print(result)

def describe_skill(skill, level="Beginner"):
    return f"{skill} - {level}"

print(describe_skill("Python"))
print(describe_skill("SQL", "Intermediate"))

def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        difficulty = "Foundational"
    else:
        difficulty = "Advanced"
    return difficulty

skills = ["Python", "SQL", "Airflow", "Spark", "Docker"]

for skill in skills:
    difficulty = classify_skill(skill)
    print(f"{skill} - {difficulty}")

long_names = [s for s in skills if len(s) > 4]   # ["SQL", "Spark"]
print(long_names)
    