#!/usr/bin/python3
"""
The `place` module supplies a class `Place`
that inherits from `BaseModel` class.
"""


from models.base_model import BaseModel
from models import place


class Place(BaseModel):
    """
    Defines a `Place` class that inherits from `BaseModel`.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
