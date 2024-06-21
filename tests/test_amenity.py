# test_amenities_api.py

import unittest
from flask import Flask
from flask_restx import Api
from amenities_api import ns as amenities_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class AmenitiesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(amenities_ns, path='/amenities')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_amenities', return_value=[])
    def test_get_amenities(self, mock_get_all):
        response = self.client.get('/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_amenity', return_value='test_id')
    def test_post_amenity(self, mock_save):
        new_amenity = {
            'name': 'Pool',
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/amenities/', json=new_amenity)
        self.assertEqual(response.status_code, 201)
        self.assertIn('amenity_id', json.loads(response.data))

    @patch.object(DataManager, 'get_amenity', return_value=None)
    def test_get_amenity_not_found(self, mock_get):
        response = self.client.get('/amenities/test_id')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_amenity', return_value=True)
    def test_delete_amenity(self, mock_delete):
        response = self.client.delete('/amenities/test_id')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_amenity', return_value=True)
    def test_put_amenity(self, mock_update):
        updated_amenity = {
            'name': 'Updated Pool',
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/amenities/test_id', json=updated_amenity)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

