#!/usr/bin/python3
"""
Defines the City class that inherits from BaseModel
"""
from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""  # id of the state
    name = ""

