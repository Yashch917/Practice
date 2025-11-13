#sing Getter and Setter methods create class bank ,constructor accholder,balance
#use getter method to access balance
#use setter method to update and add balance 
class Bank:
    def __init__(self,accholder,balance):
        self.accholder=accholder
        self.__balance=balance
        print("Account Holder:",self.accholder,", Balance:",self.__balance)
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>=0:
            self.__balance+=balance

            print("Updated Balance:", self.__balance)
        else:
            print("Invalid Balance")

b1=Bank("Sakar",5000)
print(b1.get_balance())
b1.set_balance(7000)
print(b1.get_balance())
new_balance=int(input("Enter the balance to add:"))
b1.set_balance(new_balance)
print(b1.get_balance())