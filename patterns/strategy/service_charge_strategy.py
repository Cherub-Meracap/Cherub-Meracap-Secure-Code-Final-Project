"""
This module defines the ServiceChargeStrategy Class
Date: 2025-03-10
"""
__author__ = "Cherub Meracap"
__version__ = "1.2.1"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Strategy for the service charges
    Method:
        calculate_service_charge: An abstract method to be implemented
        in the subclasses
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract calculate_service_charges method
        returns:
            float: the calculated service charge
        """
        pass
