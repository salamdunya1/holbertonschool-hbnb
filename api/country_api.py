#!/usr/bin/python3
# API for managing countries

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
import uuid
from datetime import datetime

ns = Namespace('countries', description='Operations related to countries')
data_manager = DataManager()

# Model definition for a Country
country_model = ns.model('Country', {
    'code': fields.String(required=True, description='Country code (ISO alpha-2)'),
    'name': fields.String(required=True, description='Country name'),
    'created_at': fields.DateTime(
        required=True,
        description='Date and time when the country was created'
    ),
    'updated_at': fields.DateTime(
        required=True,
        description='Date and time when the country was last updated'
    )
})


@ns.route('/')
class Countries(Resource):
    @ns.marshal_list_with(country_model)
    def get(self):
        """Fetch all countries."""
        return data_manager.get_all_countries()

    @ns.expect(country_model)
    @ns.response(201, 'Country created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new country."""
        new_country_data = request.json
        new_country_data['code'] = new_country_data['code'].upper()  # Ensure uppercase for country code
        new_country_data['created_at'] = datetime.now()
        new_country_data['updated_at'] = datetime.now()
        country_id = data_manager.save_country(new_country_data)
        return {
            'message': 'Country created successfully',
            'country_id': country_id
        }, 201


@ns.route('/<string:country_code>')
class CountryResource(Resource):
    @ns.marshal_with(country_model)
    @ns.response(404, 'Country not found')
    def get(self, country_code):
        """Fetch a country by its code."""
        country_data = data_manager.get_country(country_code)
        if country_data:
            return country_data
        else:
            ns.abort(404, "Country not found")

    @ns.response(204, 'Country deleted successfully')
    @ns.response(404, 'Country not found')
    def delete(self, country_code):
        """Delete an existing country."""
        if data_manager.delete_country(country_code):
            return '', 204
        else:
            ns.abort(404, "Country not found")

    @ns.expect(country_model)
    @ns.response(204, 'Country updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'Country not found')
    def put(self, country_code):
        """Update an existing country."""
        new_country_data = request.json
        new_country_data['code'] = country_code.upper()  # Ensure uppercase for country code
        new_country_data['updated_at'] = datetime.now()
        if data_manager.update_country(country_code, new_country_data):
            return '', 204
        else:
            ns.abort(404, "Country not found")

