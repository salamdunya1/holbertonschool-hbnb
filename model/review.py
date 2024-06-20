#!/usr/bin/python3
"""Model for representing reviews."""

import uuid
from datetime import datetime

class Review:
    def __init__(self, user_id, place_id, text):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

