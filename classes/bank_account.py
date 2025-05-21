# Filename: bank_account.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a bank account class and its functions.

import classes.transaction as transaction

# Class name: BankAccount
# Purpose: handles data for a single bank account
class BankAccount:
    name = "Default Name"
    init_balance = 0
    balance = 0
    transactions_history = [] # the history of the transactions

    # Constructor
    # Purpose: instantiates the BankAccount object
    # Input: self - the BankAccount object to be instantiated
    #        name - the account name
    #        init_balance - the starting balance for the account
    # Output: none
    # Raises: none
    def __init__(self, name, init_balance):
        self.name = name
        self.init_balance = init_balance
        self.balance = init_balance

    # to String
    # Purpose: turns the BankAccount object into a string
    # Input: self - the BankAccount object  to be printed
    # Output: a string of the user bank information
    # Raises: none
    def __str__(self):
        balance_str = '${:,.2f}'.format(self.balance)
        return f"{self.name}: {balance_str}"
    
    # Function name: add_transaction
    # Input: self - the BankAccount object
    #        type - the type of transaction (deposit, withdrawal, etc)
    #        amount - the amount in the transaction
    #        successful - a boolean of if the transaction was successful or not
    # Output: none
    # Raises: none
    def add_transaction(self, type, amount, successful):
        self.transactions_history.append(transaction.Transaction(type, amount, successful)) # create and add the new transaction

    # Function name: deposit
    # Input: self - the BankAccount object
    #        amount - the amount to be added to the balance
    # Output: none
    # Raises: none
    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("deposit", amount, True) # add the transaction to the transaction history

    # Function name: withdraw
    # Input: self - the BankAccount object
    #        amount - the amount to be removed from the balance
    # Output: the amount withdrawn if successful
    # Raises: error if not enough is in the balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction("withdrawal", amount, True)  # add the transaction to the transaction history
            return amount
        else:
            self.add_transaction("withdrawal", amount, False)  # add the transaction to the transaction history
            raise Exception("Not enough in balance to withdrawal.") # raise Exception given balance is too low
        