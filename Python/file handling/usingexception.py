try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error was found: {e}")