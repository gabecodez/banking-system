# Filename: main.py
# Author: Gabriel Sullivan
# Date: 2025-05-20
# Purpose: This script handles a basic bank account.

import classes.bank_account as bank_account
import functions.interface as interface

accounts = []

user_input = "" # for handling the user loop
# user input loop
while user_input != "exit" and user_input != "e":
    if len(accounts) > 0:
        user_input = input("Options: create, edit, display, load, exit: ").strip().lower() # get the user input

        match user_input:
            case "create":
                interface.create_bank_account_prompt(accounts)
            case "edit":
                interface.edit_account_prompt(accounts)
            case "display":
                interface.display_prompt(accounts)
            case "load":
                pass
    else:
        print("An account must be created.")
        interface.create_bank_account_prompt(accounts)

