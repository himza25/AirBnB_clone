#!/usr/bin/python3
"""
This module defines the 'State' class, which extends 'BaseModel'.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a geographical state, inheriting common attributes and
    behavior from the BaseModel.
    """
    name = ""  # The name of the state
