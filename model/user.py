#!/usr/bin/python3
"""Model for representing users."""

import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, first_name, last_name):
        self.id = uuid.uuid4()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []  # Placeholder for user's places
        self.reviews = []  # Placeholder for user's reviews

    def add_place(self, place_id):
        self.places.append(place_id)

    def add_review(self, review_id):
        self.reviews.append(review_id)

