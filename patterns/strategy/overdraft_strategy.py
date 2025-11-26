"""
This module defines the OverdraftStrategy subclass"
Date: 2025-03-10
"""
__author__ = "Cherub Meracap"
__version__ = "1.4.2"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy to apply to overdraft 
    Methods:
        __init__: Initializes overdraft_limit and overdraft_rate
        calculated_service_charges: Implements abstract method from 
        ServiceChargeStrategy superclass.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float) -> None:
        """
        Initializes a OverdraftStrategy object with the arguments
        overdraft_limit and overdraft_rate:
        Args:
            overdraft_limit (float): Maximum amount a balance can be overdrawn
            overdraft_rate (float): The rate which overdraft fees will be applied.
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Implements calculate_service_charges method with same logic
        from get_service_charges method of ChequingAccount class.
        Args:
            account: The bank account of the user
        returns:
            float
        """
        service_charge = self.BASE_SERVICE_CHARGE

        if account.balance < self.__overdraft_limit:
            service_charge = (self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance) *
                            self.__overdraft_rate)
        
        return service_charge