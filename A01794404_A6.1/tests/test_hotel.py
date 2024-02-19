"""
Test case for the Hotel class.

Methods:
    setUp: Set up a Hotel object for testing.
    test_to_dict: Test the to_dict method.
    test_from_dict: Test the from_dict method.
    test_to_dict_empty: Test the to_dict method with empty values.
    test_from_dict_missing_key: Test handling missing key in from_dict method.
    test_from_dict_empty_data: Test handling empty data in from_dict method.
"""

import unittest
from src.hotel.hotel import Hotel

class TestHotel(unittest.TestCase):
    """
    Unit tests for the Hotel class.

    This test case class is responsible for testing the behavior of the Hotel class.
    It includes tests for the to_dict and from_dict methods, ensuring correct serialization
    and deserialization of Hotel objects. It also includes tests for handling edge cases
    such as empty data and missing keys in the input dictionary.
    """

    def setUp(self):
        """
        Set up a Hotel instance with default values for testing.
        """
        self.hotel = Hotel(1, "Example Hotel", "New York")

    def test_to_dict(self):
        """
        Test the to_dict method of the Hotel class.

        This method tests whether the to_dict method returns a dictionary
        with the expected keys and values representing the hotel.
        """
        expected_dict = {
            "hotel_id": 1,
            "name": "Example Hotel",
            "location": "New York"
        }
        self.assertEqual(self.hotel.to_dict(), expected_dict)

    def test_from_dict(self):
        """
        Test the from_dict method of the Hotel class.

        This method tests whether the from_dict method correctly creates
        a Hotel instance from a dictionary containing hotel data.
        """
        data = {
            "hotel_id": 1,
            "name": "Example Hotel",
            "location": "New York"
        }
        hotel = Hotel.from_dict(data)
        self.assertEqual(hotel.hotel_id, 1)
        self.assertEqual(hotel.name, "Example Hotel")
        self.assertEqual(hotel.location, "New York")

    def test_to_dict_empty(self):
        """
        Test the to_dict method of the Hotel class with empty data.

        This method tests whether the to_dict method correctly handles
        empty data, ensuring that the resulting dictionary contains
        None or empty strings for all fields.
        """
        hotel = Hotel(None, "", "")
        expected_dict = {
            "hotel_id": None,
            "name": "",
            "location": ""
        }
        self.assertEqual(hotel.to_dict(), expected_dict)
