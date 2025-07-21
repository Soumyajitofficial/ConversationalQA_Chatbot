import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
table_info = '''
    CREATE TABLE STUDENTS
    (
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS FLOAT
    )
'''
cursor.execute(table_info)
students = [
    ('Alice Johnson', '10', 'A', 88.5),
    ('Bob Smith', '10', 'B', 76.0),
    ('Catherine Lee', '9', 'A', 91.2),
    ('David Kim', '9', 'C', 67.8),
    ('Emily Davis', '11', 'B', 84.0),
    ('Frank Moore', '11', 'A', 72.5),
    ('Grace Liu', '10', 'C', 95.3),
    ('Harry Singh', '12', 'A', 89.9),
    ('Isla Brown', '12', 'B', 78.6),
    ('Jack Wilson', '11', 'C', 82.1)
]
cursor.executemany("INSERT INTO STUDENTS (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", students)
print("INSERTED RECORDs")
data = cursor.execute("select * from STUDENTS")
for row in data:
    print(row)
connection.commit()
connection.close()
