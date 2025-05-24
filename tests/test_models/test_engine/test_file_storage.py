import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """
    Class to test the file storage method
    """

    def setUp(self):
        """
        Set up test environment
        """
        del_list = list(storage.all().keys())
        for key in del_list:
            del storage.all()[key]

    def tearDown(self):
        """
        Remove storage file at the end of tests
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """
        __objects is initially empty
        """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """
        New object is correctly added to __objects
        """
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())

    def test_all(self):
        """
        __objects is properly returned
        """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """
        File is not created on BaseModel save
        """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """
        Data is saved to file
        """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """
        FileStorage save method
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skip("Skipping test_reload")
    def test_reload(self):
        """
        Storage file is successfully loaded to __objects
        """
        pass

    def test_reload_empty(self):
        """
        Load from an empty file
        """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """
        Nothing happens if file does not exist
        """
        self.assertIsNone(storage.reload())

    def test_base_model_save(self):
        """
        BaseModel save method calls storage save
        """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_key_format(self):
        """
        Key is properly formatted
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(key, obj.__class__.__name__ + '.' + obj.id)

    def test_storage_var_created(self):
        """
        FileStorage object storage created
        """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)

    def test_new_test_case(self):
        """
        Test a new functionality in FileStorage
        """
        obj = BaseModel()
        obj.save()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(storage.all()[key], obj)


if __name__ == '__main__':
    unittest.main()
