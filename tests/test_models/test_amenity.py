#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Setup the stdout redirection to capture output.
captured_output = StringIO()
sys.stdout = captured_output


class UserTest(unittest.TestCase):
    """Test suite for Amenity-related features."""

    def test_pep8_conformance(self):
        """
        Ensure that the amenity.py script conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style checks not passed.")


# Allows for command line based test execution.
if __name__ == '__main__':
    unittest.main()
