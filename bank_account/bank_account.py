"""
Description: A class to manage BankAccount object
Author: Cherub Jamell Meracap
Date: January 21, 2025
Usage: Create an instance of BankAccount class to manage bank account objects
"""
__author__ = "Cherub Jamell Meracap"
__version__ = "1.16.5"

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject,ABC):
    """
    A class of BankAccount which has the attributes of account_number,
    client_number and balance.
    """
    ## INIT 
    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date) -> None:
        """
        Initializes a BankAccount object with account_number, client_number
        and balance.
        Args:
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number, representing the account holder.
            balance (float): A float value representing the current balance of the bank account.
            date_created (date): The date when the bank account was created.
        Local Variable:
            LARGE_TRANSACTION_THRESHOLD (float): A constant variable representing large transaction threshold
            LOW_BALANCE_LEVEL (float): A constant variable representing low balance level 
        Returns:
            None
        Raises:
            ValueError: when account_number is not an integer
            ValueError: when client_number is not an integer
        """
        # Initializes CONSTANT variables
        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        self.LOW_BALANCE_LEVEL = 50.00

        # Inherits attribute from Subject class
        super().__init__()

        # Checks if account_number is an integer
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer")
        
        # Checks if client_number is an integer
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer")
        
        # Checks if balance is not a float
        if isinstance(balance, float):
            self.__balance = balance
        else: 
            # sets default value to 0 if its not a float
            self.__balance = 0

        # Checks if date_created is not a date
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    ##Accessors
    @property
    def account_number(self) -> int:
        """
        Accessor method for account_number attribute
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor method for client_number attribute
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor method for balance attribute
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """
        Updates the balance of the bank account based on the amount received
        Amount can be a negative value.

        Args:
            amount (float): The amount received to update the balance,
            Positive values are deposit and negative values are withdraw
        
        Returns:
            None
        """
        # Checks if amount can be converted to a float
        if isinstance(amount, float):
            self.__balance += amount

        # Calls notify method to send a message
        ## Checks if balance is less than LOW_BALANCE_LEVEL
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:.2f}: on "
                               f"account {self.__account_number}.")
            
        ## Checks if amount is greater than LARGE_TRANSACTION_THRESHOLD
        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify( f"Large transaction ${amount:.2f}: on "
                               f"account {self.__account_number}.")

    def deposit(self, amount: float) -> None:
        """
        Prompts the user for an amount to deposit and adds it to the balance

        Args:
            amount (str): The amount entered by the user
        Returns: 
            None
        Raises:
            ValueError: when amount entered is non numeric
            ValueError: when a negative amount is entered
        """
        # Checks if amount is numeric
        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        # Checks if amount is negative
        if amount < 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Prompts the user for an amount to withdraw and subtracts it to the balance

        Args:
            amount (str): The amount entered by the user
        Returns:
            None
        Raises:
            ValueError: when amount entered is non numeric
            ValueError: when a negative amount is entered
            ValueError: when amount entered is greater than current balance
        """
        # Checks if amount is numeric
        if not isinstance(amount, float):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")

        # Checks if amount is a negative value
        if amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        # Checks if amount withdrawn exceeds the balance
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance.")

        # Changes the amount into a negative value and withdraws the amount
        self.update_balance(-abs(amount))

    ## __STR__ method
    def __str__(self) -> str:
        """
        Returns a string representation of account number and balance.
        Returns:
            str: A string format which include account number and balance.
        Format:
            Account Number: {account_number} Balance: {formatted balance}
        Example:
            Account Number: 20019 Balance: $6,764.67
        """
        return (f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}")
    
    ## Abstract Method
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculates the service charge based on the type of BankAccount
        Returns:
            Float: The calculated service charge.
        """
        pass

    ## Attach Method
    def attach(self, observer: Observer) -> None:
        """
        Attaches observer to the subject's list of observers
        Returns:
            None
        """
        self._observers.append(observer)
    
    ## Detach Method
    def detach(self, observer: Observer) -> None:
        """
        Removes observer from the subject's list of observers
        Returns:
            None
        """
        self._observers.remove(observer)

    ## Notify Method
    def notify(self, message: str) -> None:
        """
        Alerts all registered observers of a state change
        Returns:
            None
        """
        for observer in self._observers:
            observer.update(message)

    
    


