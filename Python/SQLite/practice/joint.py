#create database and table named studentdb.db with a table called students having following columns: student_id (primary key),name,age ,course,city
#write a python program to create a database 
import sqlite3
conn=sqlite3.connect("studentdb.db")
cur=conn.cursor()
try:
    cur.execute('''
                 CREATE TABLE students(
                 student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(30),
                 age INTEGER,
                 course VARCHAR(30),
                 city VARCHAR(30)
                 )
                    ''')
    print("Table students created successfully")
except:
    print("Table already exists")

# Q2-- Insert atleast 5 student records into the students table.
student=[
    ('Yash',22,'Computer Science','New York'),
    ('Yash 2',24,'Mathematics','Los Angeles'),
    ('Huda',23,'Physics','Chicago'),
    ('Tanaya',21,'Biology','Houston'),
    ('Party',25,'Chemistry','Phoenix')
]
cur.executemany("INSERT INTO students(name,age,course,city) VALUES(?,?,?,?)",student)

#Write a query to display all students name and their respective courses and display output using for loop
cur.execute("SELECT name, course FROM students")
print("Name || Course")
for i in cur.fetchall():
    print(i[0]," || ",i[1])

#write a qurey to show only those students who are enrolled in 'Computer Science' course
cur.execute("SELECT * FROM students WHERE course='Computer Science'")
print("\nStudents enrolled in Computer Science:")
for i in cur.fetchall():
    print(i)

#update city whose student_id is 3 to 'Pune'
cur.execute("UPDATE students SET city='Pune' WHERE student_id=3")
print("\nUpdated city for student_id 3.")
for i in cur.execute("SELECT * FROM students WHERE student_id=3"):
    print(i)

#delete student record whose student_id multiple of 5
cur.execute("DELETE FROM students WHERE student_id % 5 = 0")
print("\nDeleted student records where student_id is a multiple of 5.")
for i in cur.execute("SELECT * FROM students"):
    print(i)

#create table marks having marks_id(primary),student_id(foreign key),subject,score
try:
    cur.execute('''
                CREATE TABLE marks(
                marks_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject VARCHAR(30),
                score INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
                )
                ''')
    print("\nTable marks created successfully")
except:
    print("\nTable marks already exists")
marks_data=[
    (1,'Mathematics',85),
    (1,'Physics',90),
    (2,'Computer Science',88),
    (3,'Biology',92),
    (4,'Chemistry',80)
]
cur.executemany("INSERT INTO marks(student_id,subject,score) VALUES(?,?,?)",marks_data)
print("\nInserted marks data successfully.")

#Inner join students and marks table to display student name,course,subject,score
cur.execute('''
            SELECT students.name, students.course, marks.subject, marks.score
            FROM students
            INNER JOIN marks
            ON students.student_id = marks.student_id
            ''')
print("\n=== STUDENTS AND THEIR MARKS ===\n")
for row in cur.fetchall():
    print(f"NAME: {row[0]} | COURSE: {row[1]} | SUBJECT: {row[2]} | SCORE: {row[3]}")
conn.commit()
conn.close()