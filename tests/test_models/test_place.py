import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """
    TestPlace class to test the Place class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestPlace object
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test the city_id attribute of Place
        """
        place = Place()
        place.city_id = "abc123"
        self.assertEqual(place.city_id, "abc123")

    def test_name(self):
        """
        Test the name attribute of Place
        """
        place = Place()
        place.name = "Sample Place"
        self.assertEqual(place.name, "Sample Place")

    def test_description(self):
        """
        Test the description attribute of Place
        """
        place = Place()
        place.description = "This is a sample place."
        self.assertEqual(place.description, "This is a sample place.")

    def test_number_rooms(self):
        """
        Test the number_rooms attribute of Place
        """
        place = Place()
        place.number_rooms = 5
        self.assertEqual(place.number_rooms, 5)

    def test_number_bathrooms(self):
        """
        Test the number_bathrooms attribute of Place
        """
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        """
        Test the max_guest attribute of Place
        """
        place = Place()
        place.max_guest = 10
        self.assertEqual(place.max_guest, 10)

    def test_price_by_night(self):
        """
        Test the price_by_night attribute of Place
        """
        place = Place()
        place.price_by_night = 100.0
        self.assertEqual(place.price_by_night, 100.0)

    def test_latitude(self):
        """
        Test the latitude attribute of Place
        """
        place = Place()
        place.latitude = 40.12345
        self.assertEqual(place.latitude, 40.12345)

    def test_longitude(self):
        """
        Test the longitude attribute of Place
        """
        place = Place()
        place.longitude = -73.98765
        self.assertEqual(place.longitude, -73.98765)

    def test_amenity_ids(self):
        """
        Test the amenity_ids attribute of Place
        """
        place = Place()
        amenity_ids = [1, 2, 3]
        place.amenity_ids = amenity_ids
        self.assertEqual(place.amenity_ids, amenity_ids)

    def test_user_id(self):
        """
        Test the user_id attribute of Place
        """
        place = Place()
        place.user_id = "xyz456"
        self.assertEqual(place.user_id, "xyz456")

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of Place
        """
        pass

    def test_new_test_case(self):
        """
        Test a new functionality in Place
        """
        place = Place()
        place.new_attribute = "new value"
        self.assertTrue(hasattr(place, 'new_attribute'))
        self.assertEqual(place.new_attribute, "new value")


if __name__ == '__main__':
    unittest.main()
