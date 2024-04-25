#!/usr/bin/python3
"""
Defines the Review class that inherits from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""  # id of the place
    user_id = ""  # id of the user
    text = ""

