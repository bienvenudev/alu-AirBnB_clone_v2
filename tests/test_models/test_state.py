import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """
    TestState class to test the State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestState object
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test the name attribute of State
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of State
        """
        pass

    def test_updated_at(self):
        """
        Test the updated_at attribute of State
        """
        state = State()
        state.updated_at = "2023-06-08 12:34:56"
        self.assertEqual(state.updated_at, "2023-06-08 12:34:56")

    def test_new_test_case(self):
        """
        Test a new functionality in State
        """
        state = State()
        state.population = 1000000
        self.assertTrue(hasattr(state, 'population'))
        self.assertEqual(state.population, 1000000)

    def test_new_attribute(self):
        """
        Test the creation of a new attribute in State
        """
        state = State()
        state.new_attribute = "new value"
        self.assertTrue(hasattr(state, 'new_attribute'))
        self.assertEqual(state.new_attribute, "new value")


if __name__ == '__main__':
    unittest.main()
