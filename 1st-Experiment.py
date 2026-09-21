import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    marks INTEGER,
    department TEXT
)
""")

# Clear old data
cursor.execute("DELETE FROM students")

# Insert student data
students = [
    (1, "Rahul", 85, "CSE"),
    (2, "Priya", 92, "ECE"),
    (3, "Arun", 72, "CSE"),
    (4, "Sneha", 88, "IoT"),
    (5, "Kiran", 65, "ECE")
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    students
)

conn.commit()


# ================= USER QUESTION =================
question = input("Enter your question: ")
q = question.lower()


# ================= SQL GENERATION =================

# Search student by name
if "name" in q or "by name" in q:
    name = input("Enter student name: ")

    sql = "SELECT * FROM students WHERE LOWER(name) = LOWER(?)"
    parameters = (name,)

# Search specific student directly
elif any(name in q for name in
         ["rahul", "priya", "arun", "sneha", "kiran"]):

    names = ["rahul", "priya", "arun", "sneha", "kiran"]

    for name in names:
        if name in q:
            student_name = name
            break

    sql = "SELECT * FROM students WHERE LOWER(name) = ?"
    parameters = (student_name,)

# Marks greater than 80
elif "above 80" in q or "more than 80" in q:
    sql = "SELECT * FROM students WHERE marks > 80"
    parameters = ()

# Marks greater than 70
elif "above 70" in q or "more than 70" in q:
    sql = "SELECT * FROM students WHERE marks > 70"
    parameters = ()

# CSE students
elif "cse" in q:
    sql = "SELECT * FROM students WHERE department = 'CSE'"
    parameters = ()

# IoT students
elif "iot" in q:
    sql = "SELECT * FROM students WHERE department = 'IoT'"
    parameters = ()

# Show all students
else:
    sql = "SELECT * FROM students"
    parameters = ()


# ================= WORKFLOW =================

print("\n===== TEXT-TO-SQL WORKFLOW =====")

print("\n1. User Question:")
print(question)

print("\n2. Generated SQL:")
print(sql)

print("\n3. Executing SQL...")

cursor.execute(sql, parameters)
results = cursor.fetchall()


# ================= RESULT =================

print("\n4. Query Result:")

if results:
    for row in results:
        print(row)
else:
    print("No student found.")


print("\n===== WORKFLOW COMPLETED =====")

conn.close()