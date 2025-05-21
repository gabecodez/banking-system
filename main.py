# Filename: main.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a basic bank account.

import classes.bank_account as bank_account
import functions.interface as interface

# setup user account
name = input("Please enter your name: ") # prompt the user for their name
initial_balance = float(input("Please enter your initial balance: ")) # prompt the user for the initial balance
my_account = bank_account.BankAccount(name, initial_balance) # create user account
print("User account created.")
print(my_account) # print the account

user_input = "" # for handling the user loop

# user input loop
while user_input != "exit" or user_input != "e":
    user_input = input("Options: print, plot, deposit, withdraw, exit: ").strip().lower() # get the user input

    match user_input:
        case "print":
            interface.print_account_details(my_account) # print out the user details
        case "p":
            interface.print_account_details(my_account) # print out the user details
        case "plot":
            interface.plot_account_details(my_account)
        case "pl":
            interface.plot_account_details(my_account)
        case "deposit":
            interface.get_user_deposit(my_account) # add money
        case "d":
            interface.get_user_deposit(my_account) # add money
        case "withdraw":
            interface.get_user_withdraw(my_account) # remove money
        case "w":
            interface.get_user_withdraw(my_account) # remove money

