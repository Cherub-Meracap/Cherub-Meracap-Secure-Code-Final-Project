"""
Description: A Subclass to manage investment account object
Author: Cherub Jamell Meracap
Date: February 13, 2025
Usage: Create an instance of InvestmentAccount subclass to manage 
        investment account objects.
"""

__author__ = "Cherub Jamell Meracap"
__version__ = "1.5.6"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    A subclass of InvestmentAccount with attributes inherited
    from BankAccount superclass and attributes TEN_YEARS_AGO
    and management_fee
    """

    ## INIT
    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date, management_fee: float) -> None:
        """
        Initializes an investment account object with account_number
        client_number, balance, date_created and management_fee

        Args:
            account_number (int): bank account number inherited from 
                                  BankAccount superclass
            client_number (int): client number inherited from BankAccount superclass
            balance (float): current balance inherited from BankAccount superclass
            date_created (date): The date when the bank account was created,
                                 inherited from BankAccount superclass
            management_fee (float): flat-rate fee the bank charges for managing
                                    an InvestmentAccount
        Returns:
            None
        Raises:
            None
        """
        super().__init__(account_number, client_number, balance,
                         date_created)
        
        # Constant date type variable
        # gets current date and subtracts ten years 
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        # checks if management_fee is a float
        if isinstance(management_fee, float):
            self.__management_fee = management_fee
        else:
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(self._date_created,self.__management_fee)

    ## STR method
    def __str__(self) -> str:
        """
        Returns a string message with a string message inherited 
        from BankAccount subclass
        Returns:
            value (str): A string value of superclass, management_fee and date created
        Format:
            Account Number: {value} Balance: {value}
            Date Created: {value} Management Fee: ${value} Account Type: Investment
        Example:
            Account Number: 2341234 Balance: $19,329.21
            Date Created: 2024-01-01 Management Fee: $1.99 Account Type: Investment
        """
        value = super().__str__()
        # Checks if Investment account is more than 10 years old
        # waives fee if Investment account is 10 years old
        if self._date_created < self.TEN_YEARS_AGO:  
            fee = "Waived"
        else:
            fee = f"${self.__management_fee:.2f}"

        value += (f"\nDate Created: {self._date_created} " + 
                  f"Management Fee: {fee} Account Type: Investment")

        return value
   
    ## service charge method
    def get_service_charges(self) -> float:
        """
        Calculates the service charge of investment account
        Returns:
            Float: The service charge
        """
        return self.__strategy.calculate_service_charges(self)
