#!/usr/bin/python3
# persistence/ipersistence_manager.py

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, new_entity_data):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

