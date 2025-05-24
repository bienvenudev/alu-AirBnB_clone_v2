import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class ConsoleTestCase(unittest.TestCase):
    """
    Test for console
    """

    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.storage = models.storage

    def tearDown(self):
        del self.stdout
        del self.storage

    @unittest.skip("Skipping test_create")
    def test_create(self):
        """
        test create basic
        """
        pass

    def test_create_save(self):
        """
        test create save
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        self.assertIsNotNone(
            self.storage.all()["State.{}".format(state_id)])

    def test_create_non_existing_class(self):
        """
        test non-existing class
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create MyModel')
        self.assertEqual("** class doesn't exist **\n", self.stdout.getvalue())

    @unittest.skip("Skipping test_all")
    def test_all(self):
        """
        test all
        """
        pass

    @unittest.skip("Skipping test_update")
    def test_update(self):
        """
        test update
        """
        pass

    def test_show(self):
        """
        test show
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        self.assertIn("California", self.stdout.getvalue())

    def test_new_test_case(self):
        """
        Test a new functionality in Console
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('help quit')
        self.assertIn("Exits the program with formatting",
                      self.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
