#!/usr/bin/python3
"""
This module defines the 'Amenity' class which extends 'BaseModel'.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity with a name attribute,
    extending the functionality of BaseModel.
    """
    name = ""
