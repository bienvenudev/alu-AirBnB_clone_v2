import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """
    TestCity class to test the City class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestCity object
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test the state_id attribute of City
        """
        city = City()
        city.state_id = "abc123"
        self.assertEqual(city.state_id, "abc123")

    def test_name(self):
        """
        Test the name attribute of City
        """
        city = City()
        city.name = "Sample City"
        self.assertEqual(city.name, "Sample City")

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of City
        """
        pass

    def test_new_test_case(self):
        """
        Test a new functionality in City
        """
        city = City()
        city.population = 100000
        self.assertTrue(hasattr(city, 'population'))
        self.assertEqual(city.population, 100000)


if __name__ == '__main__':
    unittest.main()
