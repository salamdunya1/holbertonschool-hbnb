#!/usr/bin/python3
"""Model for representing amenities."""

import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

