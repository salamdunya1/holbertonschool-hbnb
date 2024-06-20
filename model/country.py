#!/usr/bin/python3
"""Model for representing countries."""

import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

