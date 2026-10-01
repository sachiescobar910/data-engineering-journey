import pandas as pd

df = pd.read_csv("skills.csv")
print(df)

print(df.head())          # first 5 rows
print(df.shape)           # (rows, columns) as a tuple
print(df.columns)         # list of column names
print(df["skill"])        # just the "skill" column
print(df[df["difficulty"] == "Advanced"])   # filter: only Advanced rows
print(df[df["difficulty"] == "Foundational"])   # filter: only Foundational rows
print(df[df["skill"] == "Python"])   # Filter df to show only rows where skill equals "Python"

df["skill_length"] = df["skill"].apply(len) # adding a new column
print(df)

df_sorted = df.sort_values("skill_length", ascending=False) # Sorts the whole table by that column, largest to smallest (ascending=False).
print(df_sorted)

df["first_letter"] = df["skill"].str[0] # adding a new column
print(df)