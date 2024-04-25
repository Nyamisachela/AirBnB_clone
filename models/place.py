#!/usr/bin/python3
"""
Defines the Place class that inherits from BaseModel
"""
from models.base_model import BaseModel

class Place(BaseModel):
    city_id = ""  # id of the city
    user_id = ""  # id of the user
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of Amenity.id

