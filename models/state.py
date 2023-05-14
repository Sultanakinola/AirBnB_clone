#!/usr/bin/python3
"""
The `state` module supplies a class `State`
that inherits from `BaseModel` class.
"""


from models.base_model import BaseModel
from models import state


class State(BaseModel):
    """
    Defines a `State` class that inherits from `BaseModel`.
    """
    name = ""
