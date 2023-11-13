#!/usr/bin/python3
"""Unittest module for the console."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Redirect stdout to capture print statements.
captured_output = StringIO()
sys.stdout = captured_output


class UserTest(unittest.TestCase):
    """Defines test cases for the console functionality."""

    def test_pep8_conformance(self):
        """
        Test that console.py is in compliance with PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style checks failed.")


# Enables running the tests from the command line.
if __name__ == '__main__':
    unittest.main()
