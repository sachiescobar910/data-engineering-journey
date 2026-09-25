profile = {
    "name": "Andres",
    "target_role": "Data Engineer"
}

skills = ["Python", "SQL", "Airflow", "Spark", "Docker"]  # expand to 5 skills

for index, skill in enumerate(skills, start=1):
    if skill == "Python" or skill == "SQL":
        difficulty = "Foundational"
    else:
        difficulty = "Advanced"
    print(f"{index}. {skill} - {difficulty}")

print(f"{profile['name']} needs to learn {len(skills)} skills to become a {profile['target_role']}, starting from Foundational to Advanced topics.")