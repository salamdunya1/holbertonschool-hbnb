#!/usr/bin/python3
# Persistence for users

from persistence.ipersistence_manager import IPersistenceManager
from model.user import User

class UserRepository(IPersistenceManager):
    def __init__(self):
        self.users = {}

    def save(self, user):
        if not hasattr(user, 'id') or user.id is None:
            user.id = str(uuid.uuid4())
        self.users[user.id] = user

    def get(self, user_id):
        return self.users.get(user_id)

    def update(self, user_id, new_user_data):
        if user_id in self.users:
            user = self.users[user_id]
            for key, value in new_user_data.items():
                setattr(user, key, value)
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

