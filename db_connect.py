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
cur.execute("SELECT * FROM skills;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()