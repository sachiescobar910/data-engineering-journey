skills = ["Python", "SQL", "Airflow", "Spark"]
skills.append("Docker")
print(skills)

profile = {
    "name": "Andres",
    "current_role": "Senior Biomedical Engineer",
    "target_role": "Data engineer",
    "years_of_experience": "6"
}

for key, value in profile.items():
    print(f"{key}: {value}")

learning_plan = [
    {"month": 1, "topic": "Python Basics"},
    {"month": 2, "topic": "SQL"},
    {"month": 3, "topic": "Data Modeling & ETL"}
    ]

for item in learning_plan:
    print(f"Month {item['month']}: {item['topic']}")