# Filename: interace.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles the functions for interacting with a BankAccount
#          object via the command line.

import matplotlib.pyplot as plt # type: ignore

# Function name: print_account_details
# Purpose: prints out the account details of a given account
# Input: BankAccount account - the BankAccount object to be printed
# Output: none
# Raises: none
def print_account_details(account):
    print(account) # print the account
    # loop through and print the transactions
    for transaction in account.transactions_history:
        print(transaction)

# Function name: plot_account_details
# Purpose: plots the account details of a given account using Matplotlib
# Input: BankAccount account - the BankAccount object to be plotted
# Output: none
# Raises: none
def plot_account_details(account):
    # check to make sure that the data to plot is not empty
    if len(account.transactions_history) <= 0:
        print("No transactions to plot found.")
        return

    x = []
    y = []

    curr_balance = account.init_balance
    # loop through and subtract the transactions from the initial balance and add to the list
    for index, transaction in enumerate(account.transactions_history):
        if transaction.successful:
            if transaction.type == "deposit":
                curr_balance += transaction.amount
            elif transaction.type == "withdrawal":
                curr_balance -= transaction.amount
            x.append(index)
            y.append(curr_balance)

    plt.plot(x, y)
    plt.title("Account Balance")
    plt.xlabel("Transactions")
    plt.ylabel("Cost")
    plt.grid(True)
    plt.show()

# Function name: get_user_deposit
# Purpose: gets the user deposit and then submits it
# Input: BankAccount account - the BankAccount object to deposit into
# Output: none
# Raises: none
def get_user_deposit(account):
    deposit_amount = float(input("Input the amount to deposit: "))
    account.deposit(deposit_amount)
    print("Amount deposited successfully.")

# Function name: get_user_withdraw
# Purpose: gets the user withdraw and then submits it
# Input: BankAccount account - the BankAccount object to withdraw from
# Output: none
# Raises: none
def get_user_withdraw(account):
    withdraw_amount = float(input("Input the amount to withdraw: "))
    try:
        account.withdraw(withdraw_amount)
    except Exception as e:
        print(e)
    else:
        print("Amount withdrawn successfully.")