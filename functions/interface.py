# Filename: interace.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles the functions for interacting with a BankAccount
#          object via the command line.

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