#!/usr/bin/python3
"""
The `city` module supplies a class `City`
that inherits from `BaseModel` class.
"""


from models.base_model import BaseModel
from models import city


class City(BaseModel):
    """
    Defines a `City` class that inherits from `BaseModel`.
    """
    state_id = ""
    name = ""
