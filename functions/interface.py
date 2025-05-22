# Filename: interace.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles the functions for interacting with a BankAccount
#          object via the command line.

import matplotlib.pyplot as plt # type: ignore
import classes.bank_account as bank_account

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

# Function name: get_new_user_name
# Purpose: gets the new user name and sets it
# Input: BankAccount account - the BankAccount object to change the name of
# Output: none
# Raises: none
def get_new_user_name(account):
    name = input("Please enter new user's name: ") # prompt the user for the name
    account.name = name

# Function name: create_bank_account_prompt
# Purpose: gets information from the user on the bank account they want to create and\
#          and then creates the user and adds it to the accounts list
# Input: accounts - a list of all the accounts
# Output: none
# Raises: none
def create_bank_account_prompt(accounts):
    # setup new user account
    name = input("Please enter new user's name: ") # prompt the user for the name
    initial_balance = float(input("Please enter the initial balance: ")) # prompt the user for the initial balance
    new_account = bank_account.BankAccount(name, initial_balance) # create user account
    print("New user account created.")
    print(new_account) # print the account
    accounts.append(new_account) # add the account to the list of accounts

# Function name: edit_account_prompt
# Purpose: handles the menu for editing account prompts
# Input: none
# Output: none
# Raises: none
def edit_account_prompt(accounts):
    # loop goes until a correct account is found
    found = False
    counter = 0 # for tracking if an account was found on the first try
    while found != True:
        if counter >= 1:
            print ("Account not found") # if no account is found in the list

        account_name = input("Enter the name of the account would you like to edit: ") # get the name of the account to edit
        for index, account in enumerate(accounts):
            if account.name == account_name:
                found = True
                break

        counter += 1

    current_account = accounts[index] # set the working account to the one tied to the name

    # get the user's choice
    user_input = ""
    while user_input != "back" and user_input != "b":
        user_input = input("Options: change name, deposit, withdraw, back: ")

        match user_input:
            case "change name":
                get_new_user_name(current_account)
            case "deposit":
                get_user_deposit(current_account)
            case "withdraw":
                get_user_withdraw(current_account)

# Function name: get_user_names
# Purpose: prompts the user to provide names of valid accounts
# Input: accounts - the list of valid account names
# Output: given_accounts - a list of the valid accounts that the user provided
# Raises: none
def get_user_names(accounts):
    valid_accounts = [] # the list of account names that will be entered by the user

    # loop goes until minimum one correct account is found
    found = False
    counter = 0 # for tracking if an account was found on the first try
    while found != True:
        if counter >= 1:
            print ("One of the accounts not found") # if no account is found in the list

        account_names = input("Enter the names of the accounts you would you like to display (separate by commas): ") # get the name of the accounts to display
        entered_account_names = account_names.split(",") # get a list of the account names

        invalid_set = False # for tracking if the user entered a wrong name somewhere
        for account_name in entered_account_names:
            account_name = account_name.strip() # remove whitespace
            valid_name = False
            for account in accounts:
                if account.name == account_name: # if name is found
                    valid_name = True
                    valid_accounts.append(account) # add the valid account to the list to be returned
            if valid_name == False: # if an item could not be found in the accounts
                invalid_set = True
                break
        if invalid_set == False:
            found = True # We were successful!
    
    return valid_accounts

# Function name: handle_print
# Purpose: handles the printing of multiple accounts
# Input: accounts - the list of BankAccount objects to loop through and print out
# Output: none
# Raises: none
def handle_print(accounts):
    for account in accounts:
        print_account_details(account)

# Function name: handle_plot
# Purpose: handles the plotting of multiple accounts
# Input: accounts - the list of BankAccount objects to loop through and plot
# Output: none
# Raises: none
def handle_plot(accounts):
    for account in accounts:
        plot_account_details(account)

# Function name: display_prompt
# Purpose: prompts the user with different display options
# Input: accounts - a list of all the user accounts
# Output: none
# Raises: none
def display_prompt(accounts):
    user_accounts = get_user_names(accounts)

    user_input = ""
    while user_input != "back" and user_input != "b":
        user_input = input("Options: print, plot, back: ") # get the user choice

        match user_input:
            case "print":
                handle_print(user_accounts) # print the provided accounts
            case "plot":
                handle_plot(user_accounts) # plot the provided accounts