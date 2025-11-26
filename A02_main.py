"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.13.1"
__credits__ = "Cherub Meracap"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date
from unittest.mock import patch
from A01_main import save_to_db


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(1212, 1001, -210.00, 
                                       date(2025, 1, 10), -200.00, 0.10)
except ValueError as e:
    print("Error occured while generating a chequing account: ", e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
save_to_db(chequing_account)
print(chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["400"]
        chequing_account.deposit()
except Exception as e:
    print("Error occured;", e)

print(chequing_account)
print(chequing_account.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(1212, 1001, 1000.10,
                                    date(2025, 1, 10), 100.00)
except ValueError as e:
    print("Error occured while generating a savings account: ", e)  


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
print(savings_account.get_service_charges())


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["950.00"]
        savings_account.withdraw()
except Exception as e:
    print("Error occured;", e)

print(savings_account)
print(savings_account.get_service_charges())


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account_1 = InvestmentAccount(1212, 1001, 1000.10,
                                        date(2025, 1, 10), 5.50)
except ValueError as e:
    print("Error occured while generating a investment account: ", e)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account_1)
print(investment_account_1.get_service_charges())


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account_2 = InvestmentAccount(1212, 1001, 1000.10,
                                        date(2013, 1, 10), 5.50)
except ValueError as e:
    print("Error occured while generating a investment account: ", e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account_2)
print(investment_account_2.get_service_charges())


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

# Chequing Account
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["0.50"]
        chequing_account.withdraw()
except Exception as e:
    print("Error occured;", e)

# Savings Account
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["2.5"]
        savings_account.withdraw()
except Exception as e:
    print("Error occured;", e)

# Investment Account 1 and 2
try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["6.00"]
        investment_account_1.withdraw()
except Exception as e:
    print("Error occured;", e)

try:
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ["0.50"]
        investment_account_2.withdraw()
except Exception as e:
    print("Error occured;", e)



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(chequing_account, "\n")
print(savings_account, "\n")
print(investment_account_1, "\n")
print(investment_account_2)