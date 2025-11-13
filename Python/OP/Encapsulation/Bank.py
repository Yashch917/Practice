#create a banking system to choose option between deposit and withdraw or loan 
class Bank1:
    a=int(input("Enter 1 for deposit, 2 for withdraw  and 3 for loan:"))
    def __init__(self,accholder,balance):
        self.accholder=accholder
        self.__balance=balance
        print("Account Holder:",self.accholder,", Balance:",self.__balance)
    def get_balance(self):
        return self.__balance
    def deposit(self,balance):
        if balance>=0:
            self.__balance+=balance

            print("Updated Balance:", balance)
        else:
            print("Invalid Balance")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn Amount:",amount)
            print("Remaining Balance:",self.__balance)
        else:
            print("Invalid Amount or Insufficient Balance")         
    def loan(self,loan_amount):
        if loan_amount>0:
            print("Loan Approved for amount:",loan_amount)
        else:
            print("Invalid Loan Amount")
b1=Bank1("Sakar",0)
for a in range(1,4):
    if Bank1.a==1:
        amt=int(input("Enter amount to deposit:"))
        b1.deposit(amt)
    elif Bank1.a==2:
        amt=int(input("Enter amount to withdraw:"))
        b1.withdraw(amt)
    elif Bank1.a==3:
        loan_amt=int(input("Enter loan amount:"))
        b1.loan(loan_amt)
    else:
        print("Invalid Option")


#