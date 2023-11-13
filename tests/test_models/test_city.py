#!/usr/bin/python3
"""Unittests for validation of the City class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Setting up buffer to capture print outputs during tests.
captured_output = StringIO()
sys.stdout = captured_output


class CityTest(unittest.TestCase):
    """Defines the test suite for the City class functionality."""

    def test_pep8_conformance_city(self):
        """
        Assesses the conformity of city.py with PEP8.
        """
        style_review = pep8.StyleGuide(quiet=True)
        result = style_review.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors detected in city.py.")


if __name__ == '__main__':
    unittest.main()
