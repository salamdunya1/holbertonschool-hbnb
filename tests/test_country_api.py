# test_country_api.py

import unittest
from flask import Flask
from flask_restx import Api
from country_api import ns as countries_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class CountriesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(countries_ns, path='/countries')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_countries', return_value=[])
    def test_get_countries(self, mock_get_all):
        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_country', return_value='test_id')
    def test_post_country(self, mock_save):
        new_country = {
            'code': 'US',
            'name': 'United States',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/countries/', json=new_country)
        self.assertEqual(response.status_code, 201)
        self.assertIn('country_id', json.loads(response.data))

    @patch.object(DataManager, 'get_country', return_value=None)
    def test_get_country_not_found(self, mock_get):
        response = self.client.get('/countries/US')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_country', return_value=True)
    def test_delete_country(self, mock_delete):
        response = self.client.delete('/countries/US')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_country', return_value=True)
    def test_put_country(self, mock_update):
        updated_country = {
            'code': 'US',
            'name': 'Updated Country',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/countries/US', json=updated_country)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

