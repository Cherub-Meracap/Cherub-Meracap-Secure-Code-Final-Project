"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "ACE Faculty"
__version__ = "1.4.0"
__credits__ = "Cherub Jamell Meracap"

import unittest
from unittest.mock import patch
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase): 
    """
    Testing data validation and attribute setting from bank_account.py
    Test Cases:
        1. Correctly set attributes to input values
        2. Balance attribute set to 0 when non-numeric balance
        3. Raises ValueError when non-number account number 
        4. Raises ValueError when non-numeric client number 
    """

    def setUp(self):
        """
        Setup run automatically before each test method and 
        provides initial values for the class attributes
        """
        self.bank_account = BankAccount(1212, 1001, 1000.10)

    def test_init_set_valid_attributes(self):
        # Arrange and Act 
        bank_account = BankAccount(1212, 1001, 1000.10)

        # Assert 
        self.assertEqual(1212, bank_account._BankAccount__account_number)
        self.assertEqual(1001, bank_account._BankAccount__client_number)
        self.assertEqual(1000.10, round(bank_account._BankAccount__balance, 2))

    def test_init_set_balance_to_zero_when_non_numeric_balance(self):
        # Arrange and Act
        bank_account = BankAccount(1212, 1001, "Non-Numeric")

        # Assert
        self.assertEqual(0, round(bank_account._BankAccount__balance, 2))

    def test_init_non_numeric_account_number_raises_exception(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("Non-Numeric", 1001, 1000.10)

    def test_init_non_numeric_client_number_raises_exception(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(1212, "Non-Numeric", 1000.10)

    """
    Testing accessor method and update balance method from bank_account.py
    Test Cases:
        1. Test correct return of account_number attribute
        2. Test correct return of client_number attribute
        3. Test correct return of balance attribute
        4. Test correct balance update when positive amount is provided
        5. Test correct balance update when negative amount is provided
        6. Test balance remains unchange when non-numeric amount is provided
    """

    def test_account_number_accessor_method(self):
        # Arrange done by setUp above
        # Act and Assert
        self.assertEqual(1212, self.bank_account.account_number)

    def test_client_number_accessor_method(self):
        # Arrange done by setUp above
        # Act and Assert
        self.assertEqual(1001, self.bank_account.client_number)
    
    def test_balance_accessor_method(self):
        # Arrange done by setUp above
        # Act and Assert
        self.assertEqual(1000.10, round(self.bank_account.balance, 2))

    def test_update_balance_method_updates_balance_with_positive_amount(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = 1100.10
        bank_account.update_balance(100.00)

        # Actual
        actual = bank_account.balance

        # Assert
        self.assertEqual(expected, actual)

    def test_update_balance_method_updates_balance_with_negative_amount(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = 900.10
        bank_account.update_balance(-100.00)

        # Actual
        actual = bank_account.balance

        # Assert
        self.assertEqual(expected, actual)

    def test_update_balance_method_not_update_balance_with_non_numeric_amount(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = 1000.10
        bank_account.update_balance("Non-numeric")

        # Actual
        actual = bank_account.balance

        # Assert
        self.assertEqual(expected, actual)

    """
    Testing deposit and withdraw method from bank_account.py
    Test Cases:
        1. Test BankAccount object's balance is correctly updated with deposit method
        2. Raises exception when a negative amount is provided in deposit
        3. Test BankAccount object's balance is correctly update with withdraw method
        4. Raises exception when a negative amount is provided in withdraw
        5. Raises exception when withdrawal is greater than current balance
    """

    def test_deposit_method_updates_balance_with_valid_amount(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = 1100.10

        with patch('builtins.input') as mock_input:
            mock_input.side_effect  = ['100.00']
            bank_account.deposit()

        # Actual
        actual = bank_account.balance

        # Assert
        self.assertEqual(expected, actual)

    def test_deposit_negative_amount_raises_exception(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = "Deposit amount: $-100.00 must be positive."

        
        # Act and Assert
        with patch('builtins.input') as mock_input:
            mock_input.side_effect  = ['-100.00']

            with self.assertRaises(ValueError) as context:
                bank_account.deposit()
        
            self.assertEqual(expected, str(context.exception))

    def test_withdraw_method_updates_balance_with_valid_amount(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = 900.10

        with patch('builtins.input') as mock_input:
            mock_input.side_effect  = ['100.00']
            bank_account.withdraw()

        # Actual
        actual = bank_account.balance

        # Assert
        self.assertEqual(expected, actual)

    def test_withdraw_negative_amount_raises_exception(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = "Withdrawal amount: $-100.00 must be positive."

        
        # Act and Assert
        with patch('builtins.input') as mock_input:
            mock_input.side_effect  = ['-100.00']

            with self.assertRaises(ValueError) as context:
                bank_account.withdraw()
        
            self.assertEqual(expected, str(context.exception))

    def test_withdraw_provided_amount_exceeds_balance_raises_exception(self):
        # Arrange
        bank_account = BankAccount(1212, 1001, 1000.10)
        expected = "Withdrawal amount: $2,000.00 must not exceed the account balance."

        
        # Act and Assert
        with patch('builtins.input') as mock_input:
            mock_input.side_effect  = ['2000.00']

            with self.assertRaises(ValueError) as context:
                bank_account.withdraw()
        
            self.assertEqual(expected, str(context.exception))

    """
    Testing __str__ method from bank_account.py
    Test Cases:
        1. Correctly return string message in proper formatting
    """

    def test_str_method_correct_format(self):
        # Arrange done by setUp above
        # Act and Assert
        self.assertEqual("Account Number: 1212 Balance: $1000.10", str(self.bank_account))

            

