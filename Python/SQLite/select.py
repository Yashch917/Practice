# SELECT query in SQLite. This is used to read or view data from a table.
# Basic SELECT Syntax
# SELECT column1, column2, ...FROM table_name;

#     * → Select all columns

#     FROM → Specifies which table to read from
 
# a) Select all columns

# SELECT * FROM student;

# This will display all rows and columns (st_id, st_name, st_class, st_email) 

# from the student table.
 
# b) Select specific columns

# SELECT st_name, st_email FROM student;

# This shows only name and email of students.
 
# c) Select with condition (WHERE clause)

# SELECT * FROM student WHERE st_class = 'B.E.';

# Only students in B.E. class will be shown.
 
# d) Order the results

# SELECT * FROM student ORDER BY st_name ASC;

# ASC → ascending order (A → Z)

# DESC → descending order (Z → A)
 
# e) Limit the number of rows

# SELECT * FROM student LIMIT 5;
# Shows only first 5 rows.
# use cursor when we want to use multiple queries.
# fetchall() = Fetches all rows from the result of the query
# fetchone() = Fetches only the next single row
# fetchmany(size) = Fetches the next ‘size’ number of rows
import sqlite3
conn=sqlite3.connect("sqlite.db")

cur=conn.cursor()
print("st_id | st_name | st_class | st_email")
cur.execute("SELECT * FROM student;")
for i in cur.fetchall():
    print(i)

cur.execute("SELECT st_name FROM student;")
print("\nStudent Names:")
for i in cur.fetchall():
    print(i)

cur.execute("SELECT * FROM student WHERE  st_email LIKE '%@gmail.com';")
print("\nDetails of student whose mail is '@gmail.com':")
for i in cur.fetchall():
    print(i)

cur.execute("SELECT * FROM student ORDER BY st_name ASC;")
print("\nStudents in ascending order of names:")
for i in cur.fetchall():
    print(i)


cur.execute("SELECT * FROM student ORDER BY st_id DESC;")
print("\nStudents in descending order of IDs:")
for i in cur.fetchall():
    print(i)

#limit the number of results
cur.execute("SELECT * FROM student LIMIT 5;")
print("\nFirst 5 students:")
for i in cur.fetchall():
    print(i)

cur.execute("SELECT * FROM student;")
print("\nUsing fetchone():")
for i in range(1,9):
    print(cur.fetchone())
    i+=i

cur.execute("SELECT *  FROM student;")
print("\nUsing fetchmany(3):")
for i in cur.fetchmany(3):
    print(i)