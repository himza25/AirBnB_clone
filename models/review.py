#!/usr/bin/python3
"""
This module introduces the Review class as a subclass of BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class represents a review by a user, including references
    to the place and the user, as well as the review text itself.
    """
    place_id = ""  # ID of the place being reviewed
    user_id = ""  # ID of the user who wrote the review
    text = ""  # Content of the review
