#!/usr/bin/python3
"""
Unit testing module for BaseModel class.
"""
import unittest
import pep8
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
import sys
from unittest.mock import patch

# Redirect stdout to capture output for evaluation.
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTest(unittest.TestCase):
    """
    Contains tests for BaseModel functionality.
    """
    def test_pep8_conformance(self):
        """
        Validates PEP8 rules compliance for BaseModel and __init__.py.
        """
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(["models/base_model.py",
                                          "models/__init__.py"])
        self.assertEqual(result.total_errors, 0,
                         "Code style violations found.")

    def test_all_method(self):
        """
        Verifies the all() method returns all objects correctly.
        """
        for key, obj in storage.all().items():
            self.assertIsInstance(obj, eval(key.split(".")[0]))

    def test_new_instance(self):
        """Tests if a new instance is created properly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_attribute(self):
        """Checks the type of the id attribute."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_id_uniqueness(self):
        """
        Ensures different instances have unique ids.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_string_representation(self):
        """
        Confirms string representation matches expected format.
        """
        obj = BaseModel()
        expected_format = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_format)

    def test_created_at_attribute(self):
        """Validates the type of created_at attribute."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_attribute(self):
        """
        Tests updated_at attribute changes after save.
        """
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()
