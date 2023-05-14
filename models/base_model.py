#!/usr/bin/python3
"""
The `base_model` module is our base class for other
classes.
"""


import models
from datetime import datetime
import uuid


class BaseModel:
    """
    A class that defines all common attributes and methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instance of the class.

        Args:
        args - variable number of positional args
        kwargs - variable number of key-word args
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            fm = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], fm)
                if key != "__class__":
                    setattr(self, key, value)


    def __str__(self):
        """
        Prints class name, id and dictionary representation
        of the class.
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        fm = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime(fm)
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict["__class__"] = self.__class__.__name__
        
        return(new_dict)
