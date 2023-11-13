#!/usr/bin/python3
"""
Comprehensive tests for the custom console.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Tests for the HBNB console."""

    def setUp(self):
        """Set up the tests."""
        self.cli = HBNBCommand()

    def create(self, cls_name):
        """Helper method to create and return a new instance ID."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("create {}".format(cls_name))
            return fake_out.getvalue().strip()

    def test_quit_command(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            with self.assertRaises(SystemExit):
                self.cli.onecmd("quit")

    def test_EOF_command(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            with self.assertRaises(SystemExit):
                self.cli.onecmd("EOF")

    def test_create_command(self):
        """Test the create command."""
        new_id = self.create("BaseModel")
        self.assertIsNotNone(storage.all()["BaseModel." + new_id])

    def test_show_command(self):
        """Test the show command."""
        new_id = self.create("BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.cli.onecmd("show BaseModel {}".format(new_id))
            self.assertIn(new_id, fake_out.getvalue().strip())

    def test_destroy_command(self):
        """Test the destroy command."""
        new_id = self.create("BaseModel")
        self.cli.onecmd("destroy BaseModel {}".format(new_id))
        self.assertNotIn("BaseModel." + new_id, storage.all())

    def test_all_command(self):
        """Test the all command."""
        self.create("BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.cli.onecmd("all BaseModel")
            self.assertIn("BaseModel", fake_out.getvalue().strip())

    def test_update_command(self):
        """Test the update command."""
        new_id = self.create("BaseModel")
        self.cli.onecmd('update BaseModel {} first_name "Betty"'
                        .format(new_id))
        obj = storage.all()["BaseModel." + new_id]
        self.assertIn("Betty", obj.first_name)

    def test_count_command(self):
        """Test the count command."""
        count_start = storage.count("BaseModel")
        self.create("BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.cli.onecmd("BaseModel.count()")
            count_end = int(fake_out.getvalue().strip())
        self.assertEqual(count_start + 1, count_end)

    def tearDown(self):
        """Tear down the tests."""
        all_objs = storage.all()
        for key in list(all_objs.keys()):
            del all_objs[key]
        storage.save()


if __name__ == "__main__":
    unittest.main()
