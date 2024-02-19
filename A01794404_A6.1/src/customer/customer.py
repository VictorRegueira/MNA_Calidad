"""
This module defines a Customer class representing a customer in a Customer Management System.

Attributes:
    customer_id (int): The unique identifier for the customer.
    name (str): The name of the customer.
    email (str): The email address of the customer.

Methods:
    __init__: Initializes a new Customer object.
    to_dict: Converts the customer object to a dictionary.
    from_dict: Creates a Customer object from a dictionary.
    save_to_file: Saves a list of customers to a JSON file.
"""


import json

class Customer:
    """Represents a customer in a Customer Management System.

    Attributes:
        customer_id (int): The unique identifier for the customer.
        name (str): The name of the customer.
        email (str): The email address of the customer.
    """

    def __init__(self, customer_id, name, email):
        """Initializes a new Customer object.

        Args:
            customer_id (int): The unique identifier for the customer.
            name (str): The name of the customer.
            email (str): The email address of the customer.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts the customer object to a dictionary.

        Returns:
            dict: A dictionary containing customer details.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        """Creates a Customer object from a dictionary.

        Args:
            data (dict): A dictionary containing customer details.

        Returns:
            Customer: A new Customer object.
        """
        return Customer(data["customer_id"], data["name"], data["email"])

    @staticmethod
    def save_to_file(customers, filename='customers.json'):
        """Saves a list of customers to a JSON file.

        Args:
            customers (list): A list of Customer objects.
            filename (str, optional): The filename to save the data. Defaults to 'customers.json'.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([customer.to_dict() for customer in customers], file)
            