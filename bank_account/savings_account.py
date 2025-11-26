"""
Description: A Subclass to manage savings account object
Author: Cherub Jamell Meracap
Date: February 15, 2025
Usage: Create an instance of SavingsAccount subclass to manage 
        savings account objects.
"""

__author__ = "Cherub Jamell Meracap"
__version__ = "1.4.3"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    A subclass of SavingsAccount with attributes inherited
    from BankAccount superclass and SERVICE_CHARGE_PREMIUM
    and minimum_balance.
    """

    ## INIT
    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date, minimum_balance: float) -> None:
        """
        Initializes an savings account object with account_number
        client_number, balance, date_created and minimum_balance

        Args:
            account_number (int): bank account number inherited from 
                                  BankAccount superclass
            client_number (int): client number inherited from BankAccount superclass
            balance (float): current balance inherited from BankAccount superclass
            date_created (date): The date when the bank account was created,
                                 inherited from BankAccount superclass
            minimum_balance (float): The minimum a balance can be before futher charges
                                    are applied.
        Returns:
            None
        Raises:
            None
        """
        super().__init__(account_number, client_number, balance,
                         date_created)

        # checks if minimum_balance is a float 
        # Uses if isinstance to check for data type
        if isinstance(minimum_balance, float):
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 50.00

        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

    ## STR method
    def __str__(self) -> str:
        """
        Returns a string message with a string message inherited 
        from BankAccount subclass
        Returns:
            value (str): A string value from superclass and minimum balance
        Format:
            Account Number: {value} Balance: {value}
            Minimum Balance: {value} Account Type: Savings
        Example:
            Account Number: 9483914 Balance: $1,559.49
            Minimum Balance: $50.00 Account Type: Savings
        """
        value = super().__str__()
        value += (f"\nMinimum Balance: ${self.__minimum_balance:.2f}" +
                  " Account Type: Savings")
        
        return value

    ## service charge method
    def get_service_charges(self) -> float:
        """
        Calculates the service charge of investment account
        Returns:
            Float: The service charge
        """
        return self.__strategy.calculate_service_charges(self)