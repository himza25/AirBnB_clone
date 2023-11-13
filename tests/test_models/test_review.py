#!/usr/bin/python3
"""Defines unittests for the Review class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Capture output for analysis by tests.
captured_output = StringIO()
sys.stdout = captured_output


class ReviewTest(unittest.TestCase):
    """Tests functionality of the Review class."""

    def test_pep8_conformance_review(self):
        """
        Ensures that review.py adheres to PEP8 standards.
        """
        style_checker = pep8.StyleGuide(quiet=True)
        result = style_checker.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 violations found in review.py.")


if __name__ == '__main__':
    unittest.main()
