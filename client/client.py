"""
Description: A class to manage client object
Author: Cherub Jamell Meracap
Date: January 20, 2025
Usage: Create an instance of Client class to manage client objects
"""
__author__ = "Cherub Jamell Meracap"
__version__ = "1.6.4"

from email_validator import validate_email, EmailNotValidError
from utility.file_utils import simulate_send_email
from datetime import date

class Client:
    """
    A class of Client which has the attributes of client_number,
    first_name, last_name, email_address
    """

    ## INIT
    def __init__(self, client_number: int, first_name: str, last_name: str,
                 email_address: str) -> None:
        """
        Initializes a Client object with client_number, first_name, 
        last_name, email_address.
        Args:
            client_number (int): An integer value representing the client number.
            first_name (str): A string value the client's first name.
            last_name (str): A string value the client's last name.
            email_address (str): A string value the client's email address.
        Returns:
            None
        Raises:
            ValueError: when client_number is not an integer
            ValueError: when first_name is blank
            ValueError: when last_name is blank
            EmailNotValidError: when an invalid email address is evaluated.
        """
        # Checks if client_number is an integer 
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer")
        
        # Checks if first_name is blank
        if len(first_name.strip()) == 0:
            raise ValueError("Client first name cannot be blank")
        else:
            self.__first_name = first_name
        
        # Checks if last_name is blank
        if len(last_name.strip()) == 0:
            raise ValueError("Client last name cannot be blank")
        else:
            self.__last_name = last_name

        # Checks if email is valid
        try:
            validated_email = validate_email(email_address, check_deliverability= False)
            self.__email_address = validated_email.normalized
        except EmailNotValidError as e:
            # Sets a default email if email is invalid
            self.__email_address = "email@pixell-river.com"

    ## Accessors
    @property
    def client_number(self) -> int:
        """
        Accessor method for client_number attribute
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor method for first_name attribute
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor method for last_name attribute
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor method for email_address attribute
        """
        return self.__email_address
    
    ## __STR__ method
    def __str__(self) -> str:
        """
        Returns a string representation of a Client object
        Returns:
            str: A string representation of client
            Format: 
                {last_name}, {first_name} [{client_number}] - {email_address}
            Example:
                Clark, Susan [1010] - susanclark@pixell.com
        """
        return (f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}")
    
    ## update method
    def update(self, message: str) -> None:
        """
        Implements update method from Observer class
        calls simulate_send_email function from file_utils.py
        Returns:
            None
        """
        simulate_send_email(self.__email_address, 
                            f"ALERT: Unusual Activity: {date.today()}",
                            f"Notification for {self.__client_number}: {self.__first_name} " 
                            f"{self.__last_name}: {message}")