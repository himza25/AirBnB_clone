#!/usr/bin/python3
"""
Unittests for console.py.
"""
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """Defines test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the test client and file storage for the tests."""
        self.cli = HBNBCommand()
        self.file_storage = create_autospec(storage)

    def tearDown(self):
        """Clean up actions."""
        pass

    def test_quit(self):
        """Test quit command - it should return True."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_quit(None))

    def test_EOF(self):
        """Test EOF command - it should return True."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_EOF(None))

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("BaseModel")
            self.assertIn("BaseModel", storage.all().keys())

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.do_show(f"BaseModel {obj_id}")
            self.assertIn(obj_id, f.getvalue().strip())

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.do_destroy(f"BaseModel {obj_id}")
            self.assertNotIn(obj_id, storage.all())

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_all("BaseModel")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.do_update(f"BaseModel {obj_id} name \"HBNB\"")
            obj = storage.all()["BaseModel." + obj_id]
            self.assertEqual("HBNB", obj.name)

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.emptyline()
            self.assertEqual('', f.getvalue().strip())

    def test_unknown(self):
        """Test the default method for unknown command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.default("unknown")
            self.assertIn("*** Unknown syntax", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
