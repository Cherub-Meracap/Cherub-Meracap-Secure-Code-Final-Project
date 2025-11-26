"""
This method defines the ManagementFeeStrategy Class
Date: 2025-03-10
"""
__author__ = "Cherub Meracap"
__version__ = "1.3.2"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy to apply management fee
    Methods:
        init: Initializes date_created, management_fee, TEN_YEARS_AGO
        calculate_service_charges: implement abstract method from
        ServiceChargeStrategy superclass. 
    """
    def __init__(self, date_created: date, management_fee: float) -> None:
        """
        Initializes a management fee strategy object with the arguments of
        date_created and management_fee
        Args:
            date_created (date): The date when bank account was created 
            management_fee (float): flat-rate fee the bank charges for managing
                                    an InvestmentAccount
        Variable:
            TEN_YEARS_AGO (date): A constant variable that has a value of 
                                    date ten years ago
        Returns:
            None
        """
        # Constant date type variable
        # gets current date and subtracts ten years 
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charge of management fee strategy
        Returns:
            Float: The service charge
        Formula:
            Date created > 10 years:
                BASE_SERVICE_CHARGE 
            Date created < 10 years:
                BASE_SERVICE_CHARGE + management_fee
        """
        # Checks if date created is more than 10 years ago
        service_charge = self.BASE_SERVICE_CHARGE

        if self.__date_created >= self.TEN_YEARS_AGO:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return service_charge

