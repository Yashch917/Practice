#create database(robotid,name,type(flying,ground,underwater),cost,company)
import sqlite3
conn=sqlite3.connect("robot.db")
try:
    conn.execute('''
                  create table robot(
                  robotid integer Primary key AUTOINCREMENT,
                  name varchar(30),
                  type varchar(20),
                  cost integer (10),
                  company varchar(30)
             )
             ''')
except:
    print("Table already exists")
conn.close()