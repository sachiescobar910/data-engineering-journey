years_of_experience = 6

if years_of_experience < 2:
    print("Junior level")
elif years_of_experience < 5:
    print("Mid level")
elif years_of_experience < 10:
    print("Senior level")
else:
    print("Expert level")

target_role = "Data engineer"
print(f"Andres is transitioning from senior biomedical engineer to {target_role}.")

if years_of_experience > 5:
    print("Andres has solid professional experience to bring into data engineering")