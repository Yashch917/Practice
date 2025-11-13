#features robot registration choices registeration ,assign task, update task ,view report,exit
#registration: name, battery level,database connectivity
#assign task: robot id,task name
#update task: robot id,task task id,new status
#view report: list of all robots with their tasks and status show how many tasks are completed by each robot
#exit / menu system
#use exception handling for invalid inputs

import sqlite3
conn = sqlite3.connect("robtasman.db")
cur = conn.cursor()
try:
    cur.execute('''
        CREATE TABLE robots (
            robot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            robot_name VARCHAR(30),
            robot_model VARCHAR(20),
            battery_level INTEGER
        )
    ''')
    print("Table 'robots' created successfully.")
except :
    print("Table 'robots' already exists.")
try:
    cur.execute('''
        CREATE TABLE tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            robot_id INTEGER,
            task_name VARCHAR(30),
            status VARCHAR(20),
            FOREIGN KEY(robot_id) REFERENCES robots(robot_id)
        )
    ''')
    print("Table 'tasks' created successfully.")
except:
    print("Table 'tasks' already exists.")

class RobotTasman:
    def __init__(self):
        self.conn = sqlite3.connect("robtasman.db")
        self.cur = self.conn.cursor()

    def register_robot(self, name, model, battery):
        try:
            self.cur.execute("INSERT INTO robots (robot_name, robot_model, battery_level) VALUES (?, ?, ?)", (name, model, battery))
            self.conn.commit()
            print(f"Robot '{name}' registered successfully.")
        except Exception as e:
            print(f"Error registering robot: {e}")

    def assign_task(self, robot_id, task_name):
        try:
            self.cur.execute("INSERT INTO tasks (robot_id, task_name, status) VALUES (?, ?, ?)", (robot_id, task_name, 'Pending'))
            self.conn.commit()
            print(f"Task '{task_name}' assigned to robot ID {robot_id}.")
        except Exception as e:
            print(f"Error assigning task: {e}")

    def update_task(self, task_id, new_status):
        try:
            self.cur.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (new_status, task_id))
            self.conn.commit()
            print(f"Task ID {task_id} updated to status '{new_status}'.")
        except Exception as e:
            print(f"Error updating task: {e}")

    def view_report(self):
        try:
            self.cur.execute('''
                SELECT r.robot_id, r.robot_name, t.task_id, t.task_name, t.status
                FROM robots r
                LEFT JOIN tasks t ON r.robot_id = t.robot_id
            ''')
            report = self.cur.fetchall()
            for row in report:
                print(row)
        except Exception as e:
            print(f"Error viewing report: {e}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    tasman = RobotTasman()
    while True:
        print("\nRobot Tasman Menu:")
        print("1. Register Robot")
        print("2. Assign Task")
        print("3. Update Task")
        print("4. View Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter robot name: ")
            model = input("Enter robot model: ")
            battery = int(input("Enter battery level (%): "))
            tasman.register_robot(name, model, battery)
        elif choice == '2':
            robot_id = int(input("Enter robot ID: "))
            task_name = input("Enter task name: ")
            tasman.assign_task(robot_id, task_name)
        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            new_status = input("Enter new status (Pending/Completed): ")
            tasman.update_task(task_id, new_status)
        elif choice == '4':
            tasman.view_report()
        elif choice == '5':
            tasman.close()
            print("Exiting Robot Tasman.")
            break
        else:
            print("Invalid choice. Please try again.")