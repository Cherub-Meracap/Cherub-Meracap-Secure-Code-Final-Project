"""
Description: Unit tests for the ChequingAccount subclass
Author: Cherub Meracap
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

__author__ = "Cherub Meracap"
__version__ = "1.2.1"

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    """
    Testing data validation and attribute setting from chequing_account.py
    Test Cases:
        1. Correctly set attributes to input values
        2. When overdraft limit has invalid type
        3. When overdraft rate has invalid type
        4. When date created has invalid type
    """

    def test_init_set_valid_attributes(self):
        # Arrange and Act
        chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            -200.00, 0.10)

        # Assert
        self.assertEqual(1212, chequing_account._BankAccount__account_number)
        self.assertEqual(1001, chequing_account._BankAccount__client_number)
        self.assertEqual(1000.10, round(chequing_account._BankAccount__balance, 2))
        self.assertEqual(date(2025, 1, 10), chequing_account._date_created)
        self.assertEqual(-200.00, round(chequing_account._ChequingAccount__overdraft_limit, 2))
        self.assertEqual(0.10, round(chequing_account._ChequingAccount__overdraft_rate, 2))

    def test_init_set_overdraft_limit_default_value_when_invalid_type_overdraft_limit(self):
        # Arrange and Act 
        chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            "Invalid-Type", 0.10)
        
        # Assert
        self.assertEqual(-100.00, round(chequing_account._ChequingAccount__overdraft_limit, 2))

    def test_init_set_overdraft_rate_default_value_when_invalid_type_overdraft_rate(self):
        # Arrange and Act 
        chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            -200.00, "Invalid-Type")
        
        # Assert
        self.assertEqual(0.05, round(chequing_account._ChequingAccount__overdraft_rate, 2))

    def test_init_set_date_created_to_today_when_invalid_type_date_created(self):
        # Arrange and Act
        chequing_account = ChequingAccount(1212, 1001, 1000.10, "Invalid-Type", 
                            -200.00, 0.10)
        
        # Assert
        self.assertEqual(date.today(), chequing_account._date_created)
    
    """
    Testing get_service_charges function and str method from chequing_account.py
    Test Cases:
        1. Correct service charge when balance is greater than overdraft_limit
        2. Correct service charge when balance is less than overdraft_limit
        3. Correct service charge when balance is equal to overdraft_limit
        4. Correct string format output from str method
    """

    def test_correct_service_charge_balance_greater_than_overdraft_limit(self):
        # Arrange and Act 
        chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            -200.00, 0.10)
        
        # Asssert
        self.assertEqual(0.5, round(ChequingAccount.get_service_charges(chequing_account),2))

    def test_correct_service_charge_balance_less_than_overdraft_limit(self):
        # Arrange and Act
        chequing_account = ChequingAccount(1212, 1001, -210.00, date(2025, 1, 10), 
                            -200.00, 0.10)
        
        # Assert
        self.assertEqual(1.50, round(ChequingAccount.get_service_charges(chequing_account),2))

    def test_correct_service_charge_balance_equal_to_overdraft_limit(self):
        # Arrange and Act
        chequing_account = ChequingAccount(1212, 1001, -200.00, date(2025, 1, 10), 
                            -200.00, 0.10)
        
        # Assert
        self.assertEqual(0.50, round(ChequingAccount.get_service_charges(chequing_account),2))

    def test_str_method_correct_string_format_output(self):
        # Arrange and Act
        chequing_account = ChequingAccount(1212, 1001, 1000.10, date(2025, 1, 10), 
                            -200.00, 0.10)
        
        # Assert
        self.assertEqual("Account Number: 1212 Balance: $1000.10\n" +
                         "Overdraft Limit: $-200.00 Overdraft Rate: 10.00% Account Type: Chequing",
                         str(chequing_account))