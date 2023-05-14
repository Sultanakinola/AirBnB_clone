#!/usr/bin/python3
"""
The `review` module supplies a class `Review`
that inherits from `BaseModel` class.
"""


from models.base_model import BaseModel
from models import review


class Review(BaseModel):
    """
    Defines a `Review` class that inherits from `BaseModel`.
    """
    place_id = ""
    user_id = ""
    text = ""
