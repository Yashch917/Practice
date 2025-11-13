#robotics.db 
#table name is robot_status
#columns(robot_id,name,type(delivery,cleaning,etc),batterylevel,status(active,inactive)
#use exception handling
#print table robot_status created successfully
#except print table already exists
#insert data multiple robots(a,b,c)
#select query to display all robots
#select to less than 70% battery level
#delete robot whose status is inactive

import sqlite3
conn=sqlite3.connect("robotics.db")
cur=conn.cursor()
try:
    conn.execute('''
                  create table robot_status(
                  robot__id integer PRIMARY KEY AUTOINCREMENT,
                  name varchar(30),
                  type varchar(20),
                  battlevel integer(3),
                  status varchar(10)
                    )
                    ''')
    print("Table robot_status created successfully")
except:
    print("Table Already Exists")

robots=[
    ('Guard','Security',55,'active'),
    ('LISA','Sorting',80,'inactive'),
    ('KKNAG','Picking',60,'active'),
    ('Code','Programming',75,'inactive')
]
conn.executemany("INSERT INTO robot_status(name,type,battlevel,status) VALUES(?,?,?,?)",robots)
conn.commit()
#print all robots
print("--------------------------All Robots:-------------------------")
cur.execute("SELECT * FROM robot_status;")
for i in cur.fetchall():
    print(i)

#robots with battery level less than 70%
print("\n-----------------------------------Robots with battery level less than 70%:-----------------------")
cur.execute("SELECT * FROM robot_status WHERE battlevel < 70;")
for i in cur.fetchall():
    print(i)

#descending order of battery level
print("\n--------------------Robots in descending order of battery level:----------------------------")
cur.execute("SELECT * FROM robot_status ORDER BY battlevel DESC;")
for i in cur.fetchall():
    print(i)

#delete robot whose status is inactive
conn.execute("DELETE FROM robot_status WHERE status='inactive';")
conn.commit()
print("\n--------------------After deleting inactive robots:----------------------------")
cur.execute("SELECT * FROM robot_status;")
for i in cur.fetchall():
    print(i)