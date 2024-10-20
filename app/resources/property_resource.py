from flask import Blueprint, request
from app.services.property_service import PropertyService

bp = Blueprint("properties", __name__)


@bp.route('/properties', methods=['POST'])
def add_property():
    data = request.get_json()
    return PropertyService.add_property(data)


@bp.route('/properties', methods=['GET'])
def get_properties():
    return PropertyService.get_properties()


@bp.route('/properties/<int:real_state_id>', methods=['GET'])
def get_property(real_state_id):
    return PropertyService.get_property(real_state_id)


@bp.route('/properties/<int:real_state_id>', methods=['PUT'])
def update_property(real_state_id):
    data = request.get_json()
    return PropertyService.update_property(real_state_id, data)


@bp.route('/properties/<int:real_state_id>', methods=['DELETE'])
def delete_property(real_state_id):
    return PropertyService.delete_property(real_state_id)
