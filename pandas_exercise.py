import pandas as pd

def classify_skill(skill):
    if skill == "Python" or skill == "SQL":
        return "Foundational"
    else:
        return "Advanced"

try:
    df = pd.read_csv("skills.csv")
except FileNotFoundError:
    print("skills.csv not found.")
df["difficulty"] = df["skill"].apply(classify_skill)
print(df)

advanced_skills = df[df["difficulty"] == "Advanced"]
print(advanced_skills)
print(df["difficulty"].value_counts())

df.to_csv("skills_analyzed.csv", index=False)