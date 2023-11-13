#!/usr/bin/python3
"""
This module contains the foundational class for the AirBnB clone project.
"""

from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """
    Represents the base class for all models in the application.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructs a new instance of the BaseModel.

        If kwargs are provided, it initializes the instance attributes
        according to the key-value pairs, otherwise, it assigns new
        unique id and timestamps to the instance.

        Args:
            *args: Unused.
            **kwargs: Key-value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime and
        signals the storage to save changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format including special
        keys '__class__', 'created_at', and 'updated_at' with ISO formatted
        datetimes.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
