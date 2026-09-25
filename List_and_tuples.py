employee = {
    "name": "Andres",
    "role": "Senior Biomedical Engineer",
    "years_experience": 6,
    "company": "ADSCC"
}

print(employee["name"])          # "Andres" - access by key
employee["target_role"] = "Data Engineer"   # add a new key-value pair
employee["years_experience"] = 7            # update a value

for key, value in employee.items():
    print(f"{key}: {value}")

team = [
    {"name": "Andres", "role": "Data Engineer"},
    {"name": "Sara", "role": "Data Analyst"}
]

for person in team:
    print(f"{person['name']} is a {person['role']}")