class Humanoid:
    def move(self):
        print("The humanoid walks on two legs.")
class WheeledRobot:
    def move(self):
        print("The wheeled robot rolls on wheels.")
class FlyingRobot:
    def move(self):
        print("The flying in the air.")
robot=[Humanoid(),WheeledRobot(),FlyingRobot()]
for i in robot:
    i.move()
    