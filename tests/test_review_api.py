# test_review_api.py

import unittest
from flask import Flask
from flask_restx import Api
from review_api import ns as reviews_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class ReviewsApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(reviews_ns, path='/reviews')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_reviews', return_value=[])
    def test_get_reviews(self, mock_get_all):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_review', return_value='test_id')
    def test_post_review(self, mock_save):
        new_review = {
            'user_id': 'user_id',
            'place_id': 'place_id',
            'rating': 5,
            'comment': 'Great place to stay!',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 201)
        self.assertIn('review_id', json.loads(response.data))

    @patch.object(DataManager, 'get_review', return_value=None)
    def test_get_review_not_found(self, mock_get):
        response = self.client.get('/reviews/test_id')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_review', return_value=True)
    def test_delete_review(self, mock_delete):
        response = self.client.delete('/reviews/test_id')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_review', return_value=True)
    def test_put_review(self, mock_update):
        updated_review = {
            'user_id': 'user_id',
            'place_id': 'place_id',
            'rating': 4,
            'comment': 'Updated review!',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/reviews/test_id', json=updated_review)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()


