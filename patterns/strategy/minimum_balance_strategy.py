"""
This module defines the MinimumBalanceStrategy class
Date: 2025-03-10
"""
__author__ = "Cherub Meracap"
__version__ = "1.2.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for minimum balance service charge
    Methods:
        init: Initializes minimum_balance and SERVICE_CHARGE_PREMIUM
        calculate_service_charges: implement abstract method from
        ServiceChargeStrategy superclass. 
    """
    def __init__(self, minimum_balance: float) -> None:
        """
        Initializes a minimum balance strategy object with the argument 
        minimum_balance.
        Args:
            minimum_balance (float): The minimum a balance can be before further charges
                                    are applied.
        Variable:
            SERVICE_CHARGE_PREMIUM (float): A constant premium of 2.00
        Returns:
            None
        """
        self.SERVICE_CHARGE_PREMIUM = 2.00

        self.__minimum_balance = minimum_balance
    
    def calculate_service_charges(self, account: BankAccount):
        """
        Calculates the service charge of minimum balance strategy
        Returns:
            Float: The service charge
        Formula:
            balance >= minimum_balance
                service_charge = BASE_SERVICE_CHARGE
            balance < minimum_balance
                service_charge = BASE_SERVICE_CHARGE + SERVICE_CHARGE_PREMIUM
        """
        service_charge = self.BASE_SERVICE_CHARGE
        
        if account.balance < self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM

        return service_charge
