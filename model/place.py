#!/usr/bin/python3
"""Model for representing places."""

import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude,
                 host_id, number_of_rooms, bathrooms, price_per_night, max_guests):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []  # Placeholder for place's amenities
        self.reviews = []  # Placeholder for place's reviews

    def add_amenity(self, amenity_id):
        self.amenities.append(amenity_id)

    def add_review(self, review_id):
        self.reviews.append(review_id)

