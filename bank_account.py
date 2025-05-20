# Filename: bank_account.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a bank account classes and their functions.

# Class name: Transaction
# Purpose: handles data for a single transaction
class Transaction:
  type = "" # deposit, withdrawal, etc
  amount = 0 # the amount withdrawn
  successful = False # if the transaction went through or not

  # Constructor
  # Purpose: instantiates the Transaction object
  # Input: self - the Transaction object to be instantiated
  #        type - the type of transaction (deposit, withdrawal, etc)
  #        amount - the amount of money used in the transaction
  #        successful - a boolean of if the transaction was successful or not
  # Output: none
  # Raises: none
  def __init__(self, type, amount, successful):
    self.type = type
    self.amount = amount
    self.successful = successful

  # to String
  # Purpose: turns the Transaction object into a string
  # Input: self - the Transaction object to be printed
  # Output: a string of the transaction information
  # Raises: none
  def __str__(self):
    amount_str = '${:,.2f}'.format(self.amount)
    if self.successful:
      status = "successful"
    else:
      status = "unsuccessful"
    return f"{status} {self.type} of {amount_str}"

# Class name: BankAccount
# Purpose: handles data for a single bank account
class BankAccount:
  name = "Default Name"
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
    self.transactions_history.append(Transaction(type, amount, successful)) # create and add the new transaction

  # Function name: deposit
  # Input: self - the BankAccount object
  #        amount - the amount to be added to the balance
  # Output: none
  # Raises: none
  def deposit(self, amount):
    self.balance += amount
    self.add_transaction("deposit", amount, True) # add the transaction to the transaction history

  # Function name: withdrawal
  # Input: self - the BankAccount object
  #        amount - the amount to be removed from the balance
  # Output: the amount withdrawn if successful
  # Raises: error if not enough is in the balance
  def withdrawal(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      self.add_transaction("withdrawal", amount, True)  # add the transaction to the transaction history
      return amount
    else:
      self.add_transaction("withdrawal", amount, False)  # add the transaction to the transaction history
      raise Exception("Not enough in balance to withdrawal.") # raise Exception given balance is too low
    
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
  except Exception:
    print(Exception)
  else:
    print("Amount withdrawn successfully.")