"""
Description: Unit tests for the SavingsAccount subclass
Author: Cherub Meracap
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""

__author__ = "Cherub Meracap"
__version__ = "1.3.0"

import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):
    """
    Testing data validation and attribute setting from savings_account.py
    Test Cases:
        1. Correctly set attributes to input values
        2. Set minimum_balance to default value when an invalid type is provided
    """

    def test_init_set_valid_attributes(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 1000.10,
                                date(2025, 1, 10), 100.00)
        # Assert
        self.assertEqual(1212, savings._BankAccount__account_number)
        self.assertEqual(1001, savings._BankAccount__client_number)
        self.assertEqual(1000.10, round(savings._BankAccount__balance, 2))
        self.assertEqual(date(2025, 1, 10), savings._date_created)
        self.assertEqual(100.00, round(savings._SavingsAccount__minimum_balance, 2))
    
    def test_init_set_minimum_balance_default_value_when_invalid_type(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 1000.10,
                                date(2025, 1, 10), "Invalid-Type")
        # Assert
        self.assertEqual(50.00, round(savings._SavingsAccount__minimum_balance, 2))

    """
    Testing get_service_charges function from savings_account.py
    Test Cases:
        1. When balance is greater than minimum balance
        2. When balance is equal to minimum balance
        3. When balance is less than minimum balance
    """
    
    def test_correct_service_charge_when_balance_greater_than_minimum_balance(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 1000.10,
                                date(2025, 1, 10), 100.00)
        # Assert
        self.assertEqual(0.50, round(SavingsAccount.get_service_charges(savings), 2))

    def test_correct_service_charge_when_balance_equal_minimum_balance(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 100.00,
                                date(2025, 1, 10), 100.00)
        # Assert
        self.assertEqual(0.50, round(SavingsAccount.get_service_charges(savings), 2))

    def test_correct_service_charge_when_balance_less_than_minimum_balance(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 50.00,
                                date(2025, 1, 10), 100.00)
         # Assert
        self.assertEqual(2.50, round(SavingsAccount.get_service_charges(savings), 2))

    """
    Testing STR method from savings_account.py
    Test Cases:
        1. Appropriate value returned based on attribute values
    """

    def test_str_method_correct_string_output(self):
        # Arrange and Act
        savings = SavingsAccount(1212, 1001, 1000.10,
                                date(2025, 1, 10), 100.00)
        # Assert
        self.assertEqual("Account Number: 1212 Balance: $1000.10\n" +
                         "Minimum Balance: $100.00 Account Type: Savings",
                         str(savings))
