# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:22:52 2023

@author: Khazeena.Aljunaibi
"""

class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance  # Initialize balance directly as the provided initial_balance

    def deposit(self, amount):
        self.balance += amount  # Add the deposited amount to the balance

    def withdraw(self, amount):
        if self.balance >= amount:  # Check if there's enough balance to withdraw
            self.balance -= amount  # Subtract the withdrawn amount from the balance
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance  # Return the current balance

# Create a bank account for a user named "Alice" with an initial balance of 1000
alice_account = BankAccount("Alice", 1000)

# Deposit 500 into Alice's account
alice_account.deposit(500)

# Withdraw 200 from Alice's account
alice_account.withdraw(200)

# Check Alice's account balance
balance = alice_account.check_balance()
print(f"Balance for {alice_account.name}: {balance}")

        