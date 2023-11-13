#!/usr/bin/python3
"""
Defines the Place class, a descendant of BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class inherits from BaseModel and encapsulates details
    about a place such as location, attributes, and associated users.
    """
    city_id = ""  # Id of the city where the place is located
    user_id = ""  # Id of the user that owns the place
    name = ""  # Name of the place
    description = ""  # Description of the place
    number_rooms = 0  # Number of rooms in the place
    number_bathrooms = 0  # Number of bathrooms in the place
    max_guest = 0  # Maximum number of guests the place can accommodate
    price_by_night = 0  # Price per night for renting the place
    latitude = 0.0  # Latitude of the place's location
    longitude = 0.0  # Longitude of the place's location
    amenity_ids = []  # List of amenity ids associated with the place
