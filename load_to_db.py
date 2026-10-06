import pandas as pd
import psycopg2
from getpass import getpass

password = getpass("Enter your postgres password: ")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="data_engineering_practice",
    user="postgres",
    password=password
)
cur = conn.cursor()

# 1. Create the table if it doesn't exist yet
cur.execute("""
    CREATE TABLE IF NOT EXISTS skills_from_csv (
        id SERIAL PRIMARY KEY,
        skill_name VARCHAR(50),
        difficulty VARCHAR(20)
    );
""")

# 2. Empty it first, so re-running the script doesn't create duplicates
cur.execute("DELETE FROM skills_from_csv;")

# 3. Extract: read the CSV with pandas
df = pd.read_csv("skills_analyzed.csv")

# 4. Load: loop through the rows and insert each one
#    (your turn - see the hints below)

for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO skills_from_csv (skill_name, difficulty) VALUES (%s, %s);",
        (row["skill"], row["difficulty"])
    )

# 5. Save the changes permanently
conn.commit()

# 6. Check the result
cur.execute("SELECT * FROM skills_from_csv;")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()