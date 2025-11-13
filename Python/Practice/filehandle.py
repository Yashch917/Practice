#user input robot name, task
with open('Robot_log.txt', 'w') as file:
    robot_name=input("Enter the robots name:")
    task=input("Enter the task assigned to this robot:")
    file.write(f"Robot Name: {robot_name}\n")
    file.write(f"Assigned Task: {task}\n")
    print("Robot details logged successfully.")
    