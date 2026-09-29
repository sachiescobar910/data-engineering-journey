def greet(name):
    return f"Hello, {name}!"

message = greet("Andres")
print(message)   # Hello, Andres!

def classify_experience(years, threshold=5):
    if years > threshold:
        return "Senior"
    return "Junior"

print(classify_experience(6))        # Senior (uses default threshold of 5)
print(classify_experience(6, 8))     # Junior (threshold overridden to 8)

def add_print(a, b):
    print(a + b)      # shows the result, but gives nothing back

def add_return(a, b):
    return a + b      # hands the result back so you can reuse it

total = add_return(2, 3) + 10   # works: 15
print(total)

# The long way
squares = []
for n in range(1, 6):
    squares.append(n * n)

# The comprehension way
squares = [n * n for n in range(1, 6)]   # [1, 4, 9, 16, 25]

skills = ["Python", "SQL", "Airflow", "Spark"]
short_names = [s for s in skills if len(s) <= 5]   # ["SQL", "Spark"]


    