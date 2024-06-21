# test_city_api.py

import unittest
from flask import Flask
from flask_restx import Api
from city_api import ns as cities_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class CitiesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(cities_ns, path='/cities')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_cities', return_value=[])
    def test_get_cities(self, mock_get_all):
        response = self.client.get('/cities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_city', return_value='test_id')
    def test_post_city(self, mock_save):
        new_city = {
            'name': 'New York',
            'country_id': 1,
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 201)
        self.assertIn('city_id', json.loads(response.data))

    @patch.object(DataManager, 'get_city', return_value=None)
    def test_get_city_not_found(self, mock_get):
        response = self.client.get('/cities/test_id')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_city', return_value=True)
    def test_delete_city(self, mock_delete):
        response = self.client.delete('/cities/test_id')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_city', return_value=True)
    def test_put_city(self, mock_update):
        updated_city = {
            'name': 'Updated City',
            'country_id': 1,
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/cities/test_id', json=updated_city)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
