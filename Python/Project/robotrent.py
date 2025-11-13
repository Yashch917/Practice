#first ask login id swaroop,password 1234 to enter to the system
#print choice for menu
#1.show available robot stock(100 robots)
#2.rent robot
#3.return robot
#4.exit
#while loop
#if 1 print available robot stock using objects
#if 2 details name of user,aadhar number,phone number,address,robot name,number of days to rent,no of robots to rent(quantity),per day rent 10000
#if more than 5 robots for 1 day discount to be given 30%
#if robot not given on time 20% per hr extra charge
#if 3 enter no of robots to return,
#if 4 print thank you for visiting
#if exit again ask login id and password
class RobotRentalSystem:
    def __init__(self):
        self.total_stock = 100
        self.available_stock = 100
        self.per_day_rent = 10000
        self.current_user = None

    def login(self):
        while True:
            user_id = input("Enter login ID: ")
            user_pass = input("Enter password: ")

            # Corrected condition
            if (user_id == "swaroop" or user_id == "yash") and user_pass == "1234":
                print("\nLogin successful!\n")
                self.current_user = user_id
                self.menu()
            else:
                print("Invalid login ID or password. Try again.\n")

    def menu(self):
        while True:
            print("\n----- ROBOT RENTAL SYSTEM MENU -----")
            print("1. Show available robot stock")
            print("2. Rent robot(s)")
            print("3. Return robot(s)")
            print("4. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_stock()
            elif choice == "2":
                self.rent_robot(self.current_user)
            elif choice == "3":
                self.return_robot()
            elif choice == "4":
                print("Thank you for visiting!\n")
                # After exit, ask login again
                self.login()
                break
            else:
                print("Invalid choice. Please try again.\n")

    def show_stock(self):
        print(f"Available robots: {self.available_stock}")

    def rent_robot(self, user_id):
        if self.available_stock <= 0:
            print("No robots available for rent.")
            return

        print("Your name:", user_id)
        aadhar = input("Enter your Aadhar number: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        robot_name = input("Enter robot name: ")
        days = int(input("Enter number of days to rent: "))
        quantity = int(input("Enter number of robots to rent: "))

        if quantity > self.available_stock:
            print("Sorry, not enough robots available.")
            return

        total_cost = self.per_day_rent * days * quantity

        # Apply 30% discount if more than 5 robots for 1 day
        if quantity > 5 and days == 1:
            discount = total_cost * 0.30
            total_cost -= discount
            print(f"30% discount applied! You saved ₹{discount}")

        print(f"Total rental cost: ₹{total_cost}")

        self.available_stock -= quantity
        print(f"{quantity} robot(s) rented successfully by {user_id}.")

    def return_robot(self):
        quantity = int(input("Enter number of robots to return: "))
        if quantity <= 0:
            print("Invalid number.")
            return

        late_hours = int(input("Enter number of hours late (0 if on time): "))
        extra_charge = 0
        if late_hours > 0:
            extra_charge = (self.per_day_rent * 0.20) * late_hours
            print(f"Late return! Extra charge: ₹{extra_charge}")

        self.available_stock += quantity
        if self.available_stock > self.total_stock:
            self.available_stock = self.total_stock

        print(f"{quantity} robot(s) returned successfully.")
        print(f"Total payable (if any late fees): ₹{extra_charge}")

# Main Program
system = RobotRentalSystem()
system.login()
