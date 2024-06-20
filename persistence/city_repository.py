#!/usr/bin/python3
# Persistence for cities


from persistence.ipersistence_manager import IPersistenceManager
from model.city import City

class CityRepository(IPersistenceManager):
    def __init__(self):
        self.cities = {}

    def save(self, city):
        if not hasattr(city, 'id') or city.id is None:
            city.id = str(uuid.uuid4())
        self.cities[city.id] = city

    def get(self, city_id):
        return self.cities.get(city_id)

    def update(self, city_id, new_city_data):
        if city_id in self.cities:
            city = self.cities[city_id]
            for key, value in new_city_data.items():
                setattr(city, key, value)
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False

