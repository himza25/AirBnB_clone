#!/usr/bin/python3
"""
This module defines the FileStorage class for serializing and
deserializing instances to and from a JSON file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Handles long-term storage of all class instances via a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Cache of deserialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of all objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object to the storage dictionary. """
        # The key is the object class name and ID
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes the objects to the JSON file. """
        obj_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file to objects if file exists. """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                del obj['__class__']
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
