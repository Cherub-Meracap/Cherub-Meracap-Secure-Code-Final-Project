"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Cherub Jamell Meracap
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "ACE Faculty"
__version__ = "1.3.0"
__credits__ = "Cherub Jamell Meracap"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """
    Testing Data Validation and Attribute setting from client.py
    Test Cases:
        1. Correctly set attributes to input values
        2. Raises ValueError exception when invalid client number
        3. Raises ValueError exception when first_name is blank
        4. Raises ValueError exception when last_name is blank
        5. Correctly set email address to defaul value when invalid
    """
    def setUp(self):
        """
        Setup run automatically before each test method and 
        provides initial values for the class attributes
        """
        self.client = Client(1001, "Paul", "Morphy", "paulmorphy@pixell-river.com")

    def test_init_set_valid_attributes(self):
        #Arrange and Act
        client = Client(1001, "Paul", "Morphy", "paulmorphy@pixell-river.com")

        #Assert
        self.assertEqual(1001, client._Client__client_number)
        self.assertEqual("Paul", client._Client__first_name)
        self.assertEqual("Morphy", client._Client__last_name)
        self.assertEqual("paulmorphy@pixell-river.com", client._Client__email_address)

    def test_init_invalid_client_number_raises_exception(self):
        #Arrange, Act and Assert
        with self.assertRaises(ValueError):
            client = Client("INVALID NUMBER", "Paul", "Morphy", "paulmorphy@pixell-river.com")

    def test_init_blank_first_name_raises_exception(self):
        #Arrange, Act and Assert
        with self.assertRaises(ValueError):
            client = Client(1001, " ", "Morphy", "paulmorphy@pixell-river.com")
    
    def test_init_blank_last_name_raises_exception(self):
        #Arrange, Act and Assert
        with self.assertRaises(ValueError):
            client = Client(1001, "Paul", " ", "paulmorphy@pixell-river.com")

    def test_init_invalid_email_address_set_email_address_to_default_value(self):
        #Arrange
        client = Client(1001, "Paul", "Morphy", "INVALID EMAIL")
        expected = "email@pixell-river.com"

        # Act and Assert
        self.assertEqual(expected, client._Client__email_address)

    """
    Testing accessor and str methods from client.py
    Test Cases:
        1. Test correct return of client_number attribute
        2. Test correct return of first_name attribute
        3. Test correct return of last_name attribute
        4. Test correct return of email_address attribute
        5. Test returns string in expected format
    """

    def test_client_number_accessor_method(self):
        #Arrange done by setUp above
        #Act and Assert
        self.assertEqual(1001, self.client.client_number)

    def test_first_name_accessor_method(self):
        #Arrange done by setUp above
        #Act and Assert
        self.assertEqual("Paul", self.client.first_name)

    def test_last_name_accessor_method(self):
        #Arrange done by setUp above
        #Act and Assert
        self.assertEqual("Morphy", self.client.last_name)
    
    def test_email_address_accessor_method(self):
        #Arrange done by setUp above
        #Act and Assert
        self.assertEqual("paulmorphy@pixell-river.com", self.client.email_address)

    def test_str_method_correct_format(self):
        #Arrange done by setUp above
        #Act and Assert
        self.assertEqual("Morphy, Paul [1001] - paulmorphy@pixell-river.com", str(self.client))


