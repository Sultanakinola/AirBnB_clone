#!/usr/bin/python3
"""
The `amenity` module supplies a class `Amenity`
that inherits from `BaseModel` class.
"""


from models.base_model import BaseModel
from models import amenity


class Amenity(BaseModel):
    """
    Defines an `Amenity` class that inherits from `BaseModel`.
    """
    name = ""
