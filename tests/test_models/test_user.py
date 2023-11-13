#!/usr/bin/python3
"""Unit test suite for the User class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Setup for capturing stdout outputs during test execution.
captured_output = StringIO()
sys.stdout = captured_output


class UserTest(unittest.TestCase):
    """Provides test cases for User class behavior."""

    def test_pep8_conformance_user(self):
        """
        Validates that user.py file follows PEP8 standard.
        """
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0,
                         "user.py does not conform to PEP8.")


if __name__ == '__main__':
    unittest.main()
