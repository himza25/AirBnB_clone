#!/usr/bin/python3
"""Unit testing suite for the Place class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Redirecting stdout to capture it for tests.
captured_output = StringIO()
sys.stdout = captured_output


class PlaceTest(unittest.TestCase):
    """Encapsulates test cases for the Place class."""

    def test_pep8_conformance_place(self):
        """
        Evaluates the PEP8 compliance of place.py.
        """
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style infractions found in place.py.")


if __name__ == '__main__':
    unittest.main()
