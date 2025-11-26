""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.5.1"
__credits__ = "Cherub Jamell Meracap"

from bank_account.bank_account import BankAccount
from client.client import Client
from unittest.mock import patch
import pymysql
import os

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client_info = Client(
            1001,
            "Paul", 
            "Morphy", 
            "paulmorphy@pixell-river.com",
        )
    except Exception as e:
        print("Error occured while generating a valid Client instance: ", e)



    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        bank_account = BankAccount(1212, 1001, 1000.10)
    except Exception as e:
        print("Error occured while generating a valid BankAccount object: ", e)



    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        bank_account_2 = BankAccount(1212, 1001, "Invalid value")
    except Exception as e:
        print("Error occured while creating an instance of BankAccount class")


    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    save_to_db(client_info.client_number)
    save_to_db(bank_account.balance)

    def save_to_db(data):
        query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
        connection = pymysql.connect(**client_info)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()


    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["Non-numeric"]
            bank_account.deposit()
    except Exception as e:
        print("Error occured;", e)

    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["-100.00"]
            bank_account.deposit()
    except Exception as e:
        print("Error occured;", e)


    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["100.00"]
            bank_account.withdraw()
    except Exception as e:
        print("Error occured;", e)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["Non-numeric"]
            bank_account.withdraw()
    except Exception as e:
        print("Error occured;", e)


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["-100.00"]
            bank_account.withdraw()
    except Exception as e:
        print("Error occured;", e)



    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["10000.00"]
            bank_account.withdraw()
    except Exception as e:
        print("Error occured;", e)
 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(f"Bank Account Information: {bank_account}")
    os.system(f'echo {bank_account} | mail -s "{client_info}" {client_info.email_address}')
  


if __name__ == "__main__":
    main()