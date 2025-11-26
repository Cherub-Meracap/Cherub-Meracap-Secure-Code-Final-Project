"""
Description: Unit tests for the InvestmentAccount subclass
Author: Cherub Meracap
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

__author__ = "Cherub Meracap"
__version__ = "1.3.1"

import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):
    """
    Testing data validation and attribute setting from investment_account.py
    Test Cases:
        1. Correctly set attributes to input values
        2. Set management_fee to default value when provided an invalid management_fee
    """

    def test_init_set_valid_attributes(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2025, 1, 10), 5.50)
        
        # Assert
        self.assertEqual(1212, investment._BankAccount__account_number)
        self.assertEqual(1001, investment._BankAccount__client_number)
        self.assertEqual(1000.10, round(investment._BankAccount__balance, 2))
        self.assertEqual(date(2025, 1, 10), investment._date_created)
        self.assertEqual(5.50, round(investment._InvestmentAccount__management_fee, 2))

    def test_init_set_management_fee_default_value_when_invalid_type(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2025, 1, 10), "Invalid-Type")
        # Assert
        self.assertEqual(2.55, round(investment._InvestmentAccount__management_fee, 2))

    """
    Testing get_service_charges function from investment_account.py
    Test Cases:
        1. Correct service charge when date created is more than 10
            years ago
        2. Correct service charge when date created is exactly
            10 years ago
        3. Correct service charge when date created within
            last 10 years.
    """

    def test_correct_service_charge_date_created_more_than_10_years_ago(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2013, 1, 10), 5.50)
        # Assert
        self.assertEqual(0.50, round(InvestmentAccount.get_service_charges(investment), 2))

    def test_correct_service_charge_date_created_exactly_10_years_ago(self):
        # Arrange and Act
        TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      TEN_YEARS_AGO, 5.50)
        # Assert
        self.assertEqual(6.00, round(InvestmentAccount.get_service_charges(investment), 2))

    def test_correct_service_charge_date_created_within_10_years_ago(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2025, 1, 10), 5.50)
        # Assert
        self.assertEqual(6.00, round(InvestmentAccount.get_service_charges(investment), 2))
    
    """
    Testing STR method from investment_account.py
    Test Cases:
        1. Display waived management fee when date created is more than 10 years ago.
        2. Display management fee when date created is within last 10 years
    """

    def test_str_method_waived_fee_when_date_created_more_than_10_years_ago(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2013, 1, 10), 5.50)
        # Assert
        self.assertEqual("Account Number: 1212 Balance: $1000.10\n" +
                         "Date Created: 2013-01-10 Management Fee: Waived " +
                         "Account Type: Investment", str(investment))
        
    def test_str_method_waived_fee_when_date_created_within_10_years_ago(self):
        # Arrange and Act
        investment = InvestmentAccount(1212, 1001, 1000.10,
                                      date(2025, 1, 10), 5.50)
        # Assert
        self.assertEqual("Account Number: 1212 Balance: $1000.10\n" +
                         "Date Created: 2025-01-10 Management Fee: $5.50 " +
                         "Account Type: Investment", str(investment))
    
