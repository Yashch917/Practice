import sqlite3
conn=sqlite3.connect("robot.db")

robo=[
    ('Guard','Ground','100000','Sakar'),
    ('Lisa','Flying','150000','Sakar'),
    ('KKNAG','Underwater','200000','Sakar'),
    ('Coding','Ground','120000','Sakar')
    
]
conn.executemany('insert into robot(name,type,cost,company)values(?,?,?,?)',robo)
conn.commit()
conn.close()