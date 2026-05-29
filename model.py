# The model structure of banking system :-
class Account():
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposite(self, deposite_amount):
        if deposite_amount != "" and deposite_amount > 0:
            self.balance += deposite_amount
            print(f"{deposite_amount} INR added successfully.")
            print(f"Total balance : {self.balance}")
            return self.balance
        else:
            print("Invalid amount!")
            return

    def withdrawl(self, withdrawl_amount):
        if withdrawl_amount != "" and withdrawl_amount > 0:
            if withdrawl_amount < self.balance: 
                self.balance -= withdrawl_amount
                print(f"{withdrawl_amount} INR withdrew. total balance : {self.balance}")
                return self.balance
            else:
                print("Insufficient balance!")
                return
        else:
            print("Invalid amount!")
            return


# Taking inputs from usr for better ui :- 
name = input("Enter name : ").strip()
if name == "":
    print("Name can't be empty!")
    exit()

try:
    account_number = int(input("Enter account number : ").strip())
    deposite_amount = int(input("Enter amount to deposite : ").strip())
    withdrawl_amount = int(input("Enter amount for withdrawl : ").strip())
except ValueError:
    print("Invalid input! Enter number only.")
    exit()



acc = Account(account_number, name)
acc.deposite(deposite_amount)
acc.withdrawl(withdrawl_amount)
