# The model structure of banking system :-
import json 
from storage import load
from storage import save


class Account():
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, deposit_amount):
        if deposit_amount != "" and deposit_amount > 0:
            data = load()
            self.balance += deposit_amount
            data[self.balance] = self.balance
            save(data)
            print(f"{deposit_amount} INR added successfully.")
            print(f"Total balance : {self.balance}")
            return self.balance
        else:
            print("Invalid amount!")
            return

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount <= self.balance: 
            self.balance -= withdrawal_amount
            data[self.balance] = 
            print(f"{withdrawal_amount} INR withdrawn. Total balance : {self.balance}")
            return self.balance
        else:
            print("Insufficient balance!")
            return

            
acc = Account("101", "krishna")
acc.deposit(1001)
