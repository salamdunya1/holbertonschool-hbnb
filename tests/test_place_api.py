import unittest
from flask import Flask
from flask_restx import Api
from place_api import ns as places_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class PlacesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(places_ns, path='/places')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_places', return_value=[])
    def test_get_places(self, mock_get_all):
        response = self.client.get('/places/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_place', return_value='test_id')
    def test_post_place(self, mock_save):
        new_place = {
            'name': 'Cozy Cottage',
            'address': '123 Maple St',
            'city_id': 'city_id',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 150.0,
            'max_guests': 4,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 201)
        self.assertIn('place_id', json.loads(response.data))

    @patch.object(DataManager, 'get_place', return_value=None)
    def test_get_place_not_found(self, mock_get):
        response = self.client.get('/places/test_id')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_place', return_value=True)
    def test_delete_place(self, mock_delete):
        response = self.client.delete('/places/test_id')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_place', return_value=True)
    def test_put_place(self, mock_update):
        updated_place = {
            'name': 'Updated Cozy Cottage',
            'address': '123 Maple St',
            'city_id': 'updated_city_id',
            'latitude': 41.7128,
            'longitude': -75.0060,
            'number_of_rooms': 4,
            'number_of_bathrooms': 3,
            'price_per_night': 200.0,
            'max_guests': 5,
            'amenity_ids': ['amenity-1', 'amenity-2'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/places/test_id', json=updated_place)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

