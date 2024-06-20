#!/usr/bin/python3
# Persistence for reviews

from persistence.ipersistence_manager import IPersistenceManager
from model.review import Review

class ReviewRepository(IPersistenceManager):
    def __init__(self):
        self.reviews = {}

    def save(self, review):
        if not hasattr(review, 'id') or review.id is None:
            review.id = str(uuid.uuid4())
        self.reviews[review.id] = review

    def get(self, review_id):
        return self.reviews.get(review_id)

    def update(self, review_id, new_review_data):
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                setattr(review, key, value)
            self.save(review)
            return True
        return False

    def delete(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False

