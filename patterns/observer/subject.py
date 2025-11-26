"""
This module defines the Subject class
Date: 2025-03-12
Usage: Maintains a list of observers and notify them of 
        state changes or events
"""

__author__ = "Cherub Meracap"
__version__ = "1.4.1"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod
class Subject(ABC):
    """
    Defines a Subject class that is responsible for maintaining a 
    list of its observers and notifying them of state
    changes or events.
    Methods:
        attach: Add a new observer to list of observers.
        detach: removes an observer from the list of observers.
        notify: alerts all registered observer of a state change
    """
    def __init__(self) -> None:
        """
        Initializes a Subject class object with a variable of 
        observers.
        Variable:
            observers (list): An empty list of observers
        Returns:
            None
        """
        self._observers = []
    
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Abstract attach method to be implemented in concrete classes
        Returns:
            None
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Abstract detach method to be implemented in concrete classes
        Returns:
            None
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Abstract notify method to be implemented in concrete classes
        Returns:
            None
        """
        pass

