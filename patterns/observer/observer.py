"""
This module defines the Observer Class
Date: 2025-03-12
"""

__author__ = "Cherub Meracap"
__version__ = "1.1.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Defines interface for all concrete observers
    Methods:
        update: notify observers when changes are made in the subject.
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method for update to be implemented in 
        concrete classes
        Returns:
            None
        """
        pass