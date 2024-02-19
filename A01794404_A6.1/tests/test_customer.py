"""
Test case for the Customer class.

Methods:
    setUp: Set up a Customer object for testing.
    test_to_dict: Test the to_dict method.
    test_from_dict: Test the from_dict method.
    test_save_to_file: Test the save_to_file method.
"""
import unittest
from src.customer.customer import Customer


class TestCustomer(unittest.TestCase):

    """Test case for the Customer class."""

    def setUp(self):
        """Set up a Customer object for testing."""
        self.customer = Customer(1, "John Doe", "john@example.com")

    def test_to_dict(self):
        """Test the to_dict method."""
        expected_dict = {
            "customer_id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        }
        self.assertEqual(self.customer.to_dict(), expected_dict)

    def test_from_dict(self):
        """Test the from_dict method."""
        data = {
            "customer_id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        }
        customer = Customer.from_dict(data)
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")

    def test_save_to_file(self):
        """Test the save_to_file method."""
        customers = [self.customer]
        filename = 'test_customers.json'
        Customer.save_to_file(customers, filename)
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            self.assertIn('"customer_id": 1', data)
            self.assertIn('"name": "John Doe"', data)
            self.assertIn('"email": "john@example.com"', data)
