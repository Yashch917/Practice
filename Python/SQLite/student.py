import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()

try:
    cur.execute('''
        CREATE TABLE college (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            dept VARCHAR(20),
            year INTEGER
        )
    ''')
    print("Table 'college' created successfully.")

except :
    print("Table 'college' already exists.")
try:
    cur.execute('''
        CREATE TABLE fees (
            fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            amount INTEGER,
            status VARCHAR(10),
            FOREIGN KEY(student_id) REFERENCES college(id)
        )
    ''')
    print("Table 'fees' created successfully.")

except:
    print("Table 'fees' already exists.")

# students = [
#     ('Yash K', 'Robotics', 3),
#     ('Yash', 'Robotics', 2),
#     ('Huda', 'Robotics', 4),
#     ('Tanaya', 'Robotics', 1)
# ]
# cur.executemany("INSERT INTO college(name, dept, year) VALUES (?, ?, ?)", students)

# fees_data = [
#     (1, 50000, 'paid'),
#     (2, 45000, 'unpaid'),
#     (3, 60000, 'paid'),
#     (4, 30000, 'unpaid')
# ]
# cur.executemany("INSERT INTO fees(student_id, amount, status) VALUES (?, ?, ?)", fees_data)

cur.execute("DELETE FROM fees WHERE student_id=1")

cur.execute("UPDATE fees SET amount=5000 WHERE student_id=2")
conn.commit()
print("Data inserted successfully.")
conn.close()