#!/usr/bin/python3
"""
Module for 'User' class, a subclass of 'BaseModel'.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class provides a template for user information, extending
    the functionality of BaseModel with user-specific attributes.
    """
    email = ""  # User's email address
    password = ""  # User's password for authentication
    first_name = ""  # User's first name
    last_name = ""  # User's last name
