#!/usr/bin/python3
"""
Test suite for the file storage mechanism.
"""
import json
import unittest
import pep8
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage
from io import StringIO
from os import remove, path
import sys
from unittest.mock import patch

# Setup to capture the stdout during the test.
captured_output = StringIO()
sys.stdout = captured_output


class FileStorageTest(unittest.TestCase):
    """Defines tests for the FileStorage class."""

    def test_pep8_style(self):
        """
        Ensures that the file storage module conforms to PEP8 standards.
        """
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Code style issues detected in file_storage.py.")

    def test_file_json(self):
        """
        Checks if JSON file creation and removal work as expected.
        """
        json_file = storage._FileStorage__file_path
        self.assertTrue(json_file.endswith('.json'))
        if path.exists(json_file):
            remove(json_file)
        self.assertFalse(path.exists(json_file))
        storage.reload()

    def test_create_instance_no_kwargs(self):
        """
        Verifies instance creation without keyword arguments.
        """
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_create_instance_with_kwargs(self):
        """
        Checks that TypeError is raised with unexpected kwargs.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_attributes(self):
        """
        Confirms that private attributes for file path and objects are correct.
        """
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_attribute_existence(self):
        """
        Ensures that necessary methods are present in the storage object.
        """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_all_method(self):
        """
        Validates the 'all' method returns all stored objects.
        """
        self.assertIsInstance(storage.all(), dict)

    def test_new_method(self):
        """
        Confirms the 'new' method adds objects to storage.
        """
        initial_count = len(storage.all())
        obj = BaseModel()
        storage.new(obj)
        new_count = len(storage.all())
        self.assertNotEqual(initial_count, new_count)

    def test_save_method(self):
        """
        Ensures that the 'save' method correctly serializes to file.
        """
        obj = BaseModel()
        obj_key = f"BaseModel.{obj.id}"
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(obj_key, data)

    def test_reload_method(self):
        """
        Tests that the 'reload' method correctly deserializes objects.
        """
        # Create new objects and save to file
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        # Reset storage and reload from file
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", storage.all())


if __name__ == '__main__':
    unittest.main()
