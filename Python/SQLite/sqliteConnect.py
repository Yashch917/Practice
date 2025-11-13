import sqlite3
conn=sqlite3.connect("sqlite.db")
try:
    conn.execute('''
                create table student(
                st_id integer PRIMARY KEY AUTOINCREMENT,
                st_name varchar(30),
                st_class varchar(10),
                st_email varchar(30)
                )
                ''')
    
except :
    print("Table already exists")
conn.close()