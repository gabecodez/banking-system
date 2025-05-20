# Filename: main.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a basic bank account.

import bank_account

name = input("Please enter your name: ") # prompt the user for their name
initial_balance = float(input("Please enter your initial balance: ")) # prompt the user for the initial balance
my_account = bank_account.BankAccount(name, initial_balance) # create user account
print("User account created.")
print(my_account) # print the account

user_input = ""

while user_input != "exit":
  user_input = input("Options: print, deposit, withdraw, exit: ") # get the user input

  match user_input:
    case "print":
      bank_account.print_account_details(my_account) # print out the user details
    case "deposit":
      bank_account.get_user_deposit(my_account) # add money
    case "withdraw":
      bank_account.get_user_withdraw(my_account) # remove money

