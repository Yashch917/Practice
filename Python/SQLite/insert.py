import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
      insert into student(st_name,st_class,st_email)
      values('Yash','BCA','yashch8105@gmail.com')
      '''
std=[
    ('yash k','Robotics','yashk@gmaiil.com'),
    ('huda','Robotics','huda@gamil.com'),
    ('taniya','Robotics','taniya@gamil.com'),
    ('karan','Robotics','karan@gamil.com'),
]
conn.execute(ins)
conn.executemany("insert into student(st_name,st_class,st_email) values(?,?,?)",std)
conn.commit()
conn.close()