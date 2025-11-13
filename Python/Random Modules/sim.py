#simulate a robot moving in a 2-D grid environment where it can move in four directions: forward, reverse, left, and right or f,r,l and r .The moves will be decided by the user input and using while loop.
direction = ['forward', 'reverse', 'left', 'right']
position = [0, 0]  # Starting at origin (0,0)
print("Initial Position:", position)
while True:
    move = input("Enter move (forward, reverse, left, right) or 'exit' to quit: ").strip().lower()
    if move == 'exit':
        print("Exiting simulation.")
        break
    elif move in direction:
        if move == 'forward':
            position[1] += 1
        elif move == 'reverse':
            position[1] -= 1
        elif move == 'left':
            position[0] -= 1
        elif move == 'right':
            position[0] += 1
        print("Current Position:", position)
    else:
        print("Invalid move. Please enter a valid direction.")