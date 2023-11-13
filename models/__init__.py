#!/usr/bin/python3
"""Initializes the package for consistent import structure."""
from .engine.file_storage import FileStorage

# Instantiate a FileStorage object and load data from file.
storage = FileStorage()
storage.reload()
