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
    def setUp(self):
        self.hotel = Hotel(1, "Example Hotel", "New York")

    def test_to_dict(self):
        expected_dict = {
            "hotel_id": 1,
            "name": "Example Hotel",
            "location": "New York"
        }
        self.assertEqual(self.hotel.to_dict(), expected_dict)

    def test_from_dict(self):
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
        hotel = Hotel(None, "", "")
        expected_dict = {
            "hotel_id": None,
            "name": "",
            "location": ""
        }
        self.assertEqual(hotel.to_dict(), expected_dict)

    def test_from_dict_missing_key(self):
        data = {
            "hotel_id": 1,
            "name": "Example Hotel"
            # Missing "location" key
        }
        with self.assertRaises(KeyError):
            hotel = Hotel.from_dict(data)

    def test_from_dict_empty_data(self):
        data = {}
        with self.assertRaises(KeyError):
            hotel = Hotel.from_dict(data)
            