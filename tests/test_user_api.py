# test_user_api.py

import unittest
from flask import Flask
from flask_restx import Api
from user_api import ns as users_ns
from data_manager import DataManager
from unittest.mock import patch
import json
from datetime import datetime

class UsersApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(users_ns, path='/users')
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_users', return_value=[])
    def test_get_users(self, mock_get_all):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    @patch.object(DataManager, 'save_user', return_value='test_id')
    def test_post_user(self, mock_save):
        new_user = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.post('/users/', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('user_id', json.loads(response.data))

    @patch.object(DataManager, 'get_user', return_value=None)
    def test_get_user_not_found(self, mock_get):
        response = self.client.get('/users/test_id')
        self.assertEqual(response.status_code, 404)

    @patch.object(DataManager, 'delete_user', return_value=True)
    def test_delete_user(self, mock_delete):
        response = self.client.delete('/users/test_id')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_user', return_value=True)
    def test_put_user(self, mock_update):
        updated_user = {
            'email': 'updated_test@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        response = self.client.put('/users/test_id', json=updated_user)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
