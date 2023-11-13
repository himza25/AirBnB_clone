#!/usr/bin/python3
"""Unit tests for the State class."""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch

# Redirect stdout for the duration of the tests.
captured_output = StringIO()
sys.stdout = captured_output


class StateTest(unittest.TestCase):
    """Series of tests for the State class functionality."""

    def test_pep8_conformance_state(self):
        """
        Confirms compliance of state.py with PEP8 protocol.
        """
        style_validator = pep8.StyleGuide(quiet=True)
        result = style_validator.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Code not aligned with PEP8 in state.py.")


if __name__ == '__main__':
    unittest.main()
