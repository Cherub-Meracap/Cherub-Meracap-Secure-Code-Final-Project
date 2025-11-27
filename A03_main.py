"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.8.0"
__credits__ = "Cherub Meracap"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client
from unittest.mock import patch
import pickle
import os


DB_Password = "My_pw123"
API_KEY = "sk-fake-api-Key"
# 2. Create a Client object with data of your choice.
client1 = Client(1001, "Paul", "Morphy", "paulmorphy@pixell-river.com")



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            -200.00, 0.10)

savings = SavingsAccount(1212, 1001, 1000.10,
                                date(2025, 1, 10), 100.00)




# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_account.attach(client1)
savings.attach(client1)




# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(1936, "Mikhail", "Tal", "mikhailtal@pixell-river.com")

savings2 = SavingsAccount(1992, 1936, 2000.10, date(2024, 2, 25), 200.00)
savings2.attach(client2)

def load_account_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except Exception as e:
        print(f"Error loading account data: ", e)



# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Performing deposits and withdraws with chequing_account
## performing deposit notifies observer of large transaction
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["10500"]
        chequing_account.deposit()
except Exception as e:
    print("Error occured:", e)

print(chequing_account)

## performing withdraw notifies observer of low balance
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["11470"]
        chequing_account.withdraw()
except Exception as e:
    print("Error occured:", e)

print(chequing_account)

### performing deposit that would not cause subject to notify observer
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["500"]
        chequing_account.deposit()
except Exception as e:
    print("Error occured:", e)

print(chequing_account)
os.system(f'echo {chequing_account} | mail -s "{chequing_account}" {chequing_account.client_number}')

# Performing deposits and withdraws with savings
## performing deposit notifies observer of large transaction
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["11000"]
        savings.deposit()
except Exception as e:
    print("Error occured:", e)

print(savings)

## performing withdraw notifies observer of low balance
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["11970"]
        savings.withdraw()
except Exception as e:
    print("Error occured:", e)

print(savings)

### performing deposit that would not cause subject to notify observer
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["500"]
        savings.deposit()
except Exception as e:
    print("Error occured:", e)

print(savings)

# Performing deposits and withdraws with savings2
## performing deposit notifies observer of large transaction
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["11000"]
        savings2.deposit()
except Exception as e:
    print("Error occured:", e)

print(savings2)

## performing withdraw notifies observer of low balance
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["12970"]
        savings2.withdraw()
except Exception as e:
    print("Error occured:", e)

print(savings2)

### performing deposit that would not cause subject to notify observer
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["500"]
        savings2.deposit()
except Exception as e:
    print("Error occured:", e)

print(savings2)


