#!/usr/bin/python3
""" Persistence for countries"""


from persistence.ipersistence_manager import IPersistenceManager
from model.country import Country

class CountryRepository(IPersistenceManager):
    def __init__(self):
        self.countries = {}

    def save(self, country):
        if not hasattr(country, 'id') or country.id is None:
            country.id = str(uuid.uuid4())
        self.countries[country.id] = country

    def get(self, country_id):
        return self.countries.get(country_id)

    def update(self, country_id, new_country_data):
        if country_id in self.countries:
            country = self.countries[country_id]
            for key, value in new_country_data.items():
                setattr(country, key, value)
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False

