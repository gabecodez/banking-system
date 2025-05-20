# Filename: transaction.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a transaction class and its functions.

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