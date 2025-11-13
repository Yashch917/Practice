#print satement welcome to kotak mahindra bank
#enter your name
#enter account type(savings/current)
#print menu
#print 1.deposit
#print 2.withdraw
#print 3.show balance
#print 4.loan
#print 5.show details
#print 6.exit
#print enter your choice
#if choice is 1
#enter amount to deposited successfully
#deposit amount is deposited
#if desposit amount is invalid print invalid amount
#if choice is 2
#enter amount to withdraw
#withdraw amount is withdrawn successfully
#if withdraw amount is invalid print invalid amount or insufficient balance
#if choice is 3
#show balance
#if choice is 4
#enter loan amount
#enter loan period(years)
#enter account type(savings/current)
#if savings lower than 1 lakh is ok, if current above 1 lakh is ok
#loan is approved for amount for period years at 10% interest
#total amount to be paid is total amount
#if choice is 5
#show account holder name
#show account type
#show balance
#loan details if any
#if choice is 6
#print thank you for banking with us

print("Welcome to Kotak Mahindra Bank")
name = input("Enter your name: ")
account_type = input("Enter account type (savings/current): ").lower()
balance = 0
loan_details = None
menu = """\nMenu:
1. Deposit
2. Withdraw
3. Show Balance
4. Loan
5. Show Details
6. Exit
"""
while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount.")
    
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Invalid amount or insufficient balance.")
    
    elif choice == '3':
        print(f"Current balance: {balance}")
    
    elif choice == '4':
        loan_amount = float(input("Enter loan amount: "))
        loan_period = int(input("Enter loan period (years): "))
        
        if (account_type == 'savings' and loan_amount <= 100000) or (account_type == 'current' and loan_amount > 100000):
            interest_rate = 0.10
            total_amount = loan_amount * (1 + interest_rate * loan_period)
            loan_details = (loan_amount, loan_period, total_amount)
            print(f"Loan approved for {loan_amount} for {loan_period} years at 10% interest.")
            print(f"Total amount to be paid: {total_amount}")

        else:
            print("Loan not approved based on account type and amount.")
    
    elif choice == '5':
        print(f"Account Holder Name: {name}")
        print(f"Account Type: {account_type}")
        print(f"Balance: {balance}")
        if loan_details:
            print(f"Loan Amount: {loan_details[0]}, Loan Period: {loan_details[1]} years, Total Amount to be Paid: {loan_details[2]}")
        else:
            print("No loan details available.")
    
    elif choice == '6':
        print("Thank you for banking with us!")
        break
    
    else:
        print("Invalid choice. Please try again.")