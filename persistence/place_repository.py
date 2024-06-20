#!/usr/bin/python3
"""Persistence for places"""

from persistence.ipersistence_manager import IPersistenceManager
from model.place import Place

class PlaceRepository(IPersistenceManager):
    def __init__(self):
        self.places = {}

    def save(self, place):
        if not hasattr(place, 'id') or place.id is None:
            place.id = str(uuid.uuid4())
        self.places[place.id] = place

    def get(self, place_id):
        return self.places.get(place_id)

    def update(self, place_id, new_place_data):
        if place_id in self.places:
            place = self.places[place_id]
            for key, value in new_place_data.items():
                setattr(place, key, value)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False

