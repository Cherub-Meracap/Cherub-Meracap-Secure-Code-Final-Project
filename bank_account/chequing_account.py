"""
Description: A Subclass to manage chequing account object
Author: Cherub Jamell Meracap
Date: February 10 , 2025
Usage: Create an instance of chequingAccount subclass to manage 
        chequing account objects.
"""

__author__ = "Cherub Jamell Meracap"
__version__ = "1.5.4"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy 
 
class ChequingAccount(BankAccount):
    """
    A subclass of ChequingAccount with attributes inherited
    from BankAccount superclass and attributes overdraft_limit
    and overdraft_rate.
    """
    ## INIT
    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 overdraft_limit: float, overdraft_rate: float) -> None:
        """
        Initializes a chequing account object with account_number
        client_number, balance, date_created, overdraft_limit and
        overdraft_rate.

        Args:
            account_number (int): bank account number inherited from 
                                  BankAccount superclass
            client_number (int): client number inherited from BankAccount superclass
            balance (float): current balance inherited from BankAccount superclass
            date_created (date): The date when the bank account was created,
                                 inherited from BankAccount superclass
            overdraft_limit (float): Maximum amount a balance can be overdrawn
                                     (below 0.00) before overdraft fees are applied
            overdraft_rate (float): The rate to which overdraft fees will be applied
        Returns:
            None
        Raises:
            None
        """
        super().__init__(account_number, client_number, balance,
                         date_created)
        # checks if overdraft_limit is a float
        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100.00

        # checks if overdraft_rate is a float
        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    ## STR method
    def __str__(self) -> str:
        """
        Returns a string message with a string message inherited 
        from BankAccount subclass, overdraft_limit, overdraft_rate
        and Account type.
        Returns:
            str: A string value of superclass, overdraft_limit, overdraft_rate
                and Account type.
        Format:
            Account Number: {value} Balance: {value}
            Overdraft limit: ${value} Overdraft Rate: {value}% Account Type: Chequing
        Example:
            Account Number: 1234567 Balance: $1,559.49
            Overdraft Limit: $-15.00 Overdrft Rate: 5.00% Account Type: Chequing
        """
        value = super().__str__()

        value += (f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate:.2%} Account Type: Chequing")

        return value
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge chequing account
        Returns:
            Float: The service charge"
        """
        return self.__strategy.calculate_service_charges(self)

        
