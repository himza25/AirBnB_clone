#!/usr/bin/python3
"""
Module defining the City class, a subclass of BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class, which extends BaseModel, includes attributes
    specific to city information within the application's context.
    """
    state_id = ""  # Identifier for the state a city belongs to
    name = ""      # Name of the city
