# When working with SQLite3 in Python, a JOIN is used to combine 

# rows from two or more tables using a common column 

# (usually a primary key–foreign key relationship).
 
# 1) Primary Key.

# A Primary Key is a unique identifier for each record (row) in a table.

# It helps the database identify each row separately 

# — no two rows can have the same primary key value.
 
# Key Points:

# It must be unique for every record.

# It cannot be NULL (empty).

# A table can have only one primary key.

# Usually, it is an ID column (like robo_id, student_id, etc.).
 
# 2) Foreign Key.

# A Foreign Key is a column in one table that links to the Primary Key of another table.

# It is used to create a relationship between two tables.
 
# Key Points:

# A Foreign Key connects two tables.

# It helps maintain data consistency — meaning only valid IDs can be used.

# The table that has the Foreign Key is the child table.

# The table that has the Primary Key is the parent table.
 
# 1) robo_details

# Stores robot information.

# | robo_id | robo_name | robo_type  |

# | ------- | --------- | ---------- |

# | 1       | ROBO-A    | Drone      |

# | 2       | ROBO-B    | Humanoid   |

# | 3       | ROBO-C    | Underwater |
 
# 2) robo_tasks

# Stores tasks assigned to robots.
 
# | task_id | robo_id | task_name    | zone   |

# | ------- | ------- | ------------ | ------ |
# | 1       | 1       | Surveillance | Zone-A |
# | 2       | 1       | Mapping      | Zone-B |
# | 3       | 2       | Delivery     | Zone-C |

import sqlite3
conn = sqlite3.connect("RDD.db")
cur = conn.cursor()

try:
    cur.execute('''
        CREATE TABLE robo_details (
            robo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            robo_name VARCHAR(30),
            robo_type VARCHAR(20)
        )
    ''')
    print("Table 'robo_details' created successfully.")

except :
    print("Table 'robo_details' already exists.")
try:
    cur.execute('''
        CREATE TABLE robo_tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            robo_id INTEGER,
            task_name VARCHAR(30),
            zone VARCHAR(20),
            FOREIGN KEY(robo_id) REFERENCES robo_details(robo_id)
        )
    ''')
    print("Table 'robo_tasks' created successfully.")

except:
    print("Table 'robo_tasks' already exists.")

robots = [
    ('ROBO-A', 'Drone'),
    ('ROBO-B', 'Humanoid'),
    ('ROBO-C', 'Underwater')
]
cur.executemany("INSERT INTO robo_details(robo_name, robo_type) VALUES (?, ?)", robots)

tasks = [
    (1, 'Surveillance', 'Zone-A'),
    (1, 'Mapping', 'Zone-B'),
    (2, 'Delivery', 'Zone-C')
]
cur.executemany("INSERT INTO robo_tasks(robo_id, task_name, zone) VALUES (?, ?, ?)", tasks)
conn.commit()
print("Data inserted successfully.")

cur.execute('''
    SELECT robo_details.robo_id,robo_details.robo_name,robo_details.robo_type,
            robo_tasks.task_name,robo_tasks.zone
    FROM robo_details
    INNER JOIN robo_tasks
    ON robo_details.robo_id=robo_tasks.robo_id
    ''')

rows=cur.fetchall()
print("\n=== ROBOTS AND THEIR TASKS ===\n")
for row in rows:
    print(f"ROBOT ID: {row[0]} | NAME: {row[1]} | TYPE: {row[2]} | TASK: {row[3]} | ZONE: {row[4]}")



#left join returns all records from the left table (robo_details), and the matched records from the right table (robo_tasks).
cur.execute('''
    SELECT robo_details.robo_id,robo_details.robo_name,robo_details.robo_type,
            robo_tasks.task_name,robo_tasks.zone
    FROM robo_details
    LEFT JOIN robo_tasks
    ON robo_details.robo_id=robo_tasks.robo_id
    ''')

row1=cur.fetchall()
print("\n=== LEFT JOIN: ALL ROBOTS AND THEIR TASKS (IF ANY) ===\n")
for r in row1:
    print(f"ROBOT ID: {r[0]} | NAME: {r[1]} | TYPE: {r[2]} | TASK: {r[3]} | ZONE: {r[4]}")

conn.close()