#!/usr/bin/python3
"""
The `file_storage` module defines our file storage.
"""


from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """
    A class implementing the file storage methods.
    """
    __file_path = "file.json"
    __objects = {}
    cls_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __object (dictionary) the obj with key.

        Args:
        obj - value to set on the __object key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __object (dictionary) to the JSON
        file (path: __file_path).
        """
        dictionary = {}
        for key, value in self.__objects.items():
            if hasattr(value, 'to_dict'):
                dictionary[key] = value.to_dict()
            else:
                dictionary[key] = value

        with open(self.__file_path, "w", encoding="UTF-8") as jfile:
            json.dump(dictionary, jfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists.
        But nothing when it does not exist.
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                for key, value in json.load(file).items():
                    obj = self.cls_dict[value["__class__"]](**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
