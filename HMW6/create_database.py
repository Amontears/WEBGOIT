import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
''')

groups = [f'Группа {i + 1}' for i in range(3)]
cursor.executemany('INSERT INTO groups (name) VALUES (?)', [(group,) for group in groups])

teachers = [fake.name() for _ in range(5)]
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', [(teacher,) for teacher in teachers])

subjects = [fake.word().capitalize() for _ in range(5)]
for subject in subjects:
    teacher_id = random.randint(1, 5)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

students = []
for _ in range(30):
    name = fake.name()
    group_id = random.randint(1, 3)
    students.append((name, group_id))
cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)

for student_id in range(1, 31):
    num_grades = random.randint(1, 20)
    for _ in range(num_grades):
        subject_id = random.randint(1, 5)
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, grade, date))

conn.commit()
conn.close()

print("База данных создана и заполнена данными.")
