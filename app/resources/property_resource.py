from flask import Blueprint, request
from app.controllers.property_controller import PropertyController

bp = Blueprint("properties", __name__)


@bp.route('/properties', methods=['POST'])
def add_property():
    data = request.get_json()
    return PropertyController.add_property(data)


@bp.route('/properties', methods=['GET'])
def get_properties():
    return PropertyController.get_properties()


@bp.route('/properties/<int:real_state_id>', methods=['GET'])
def get_property(real_state_id):
    return PropertyController.get_property(real_state_id)


@bp.route('/properties/<int:real_state_id>', methods=['PUT'])
def update_property(real_state_id):
    data = request.get_json()
    return PropertyController.update_property(real_state_id, data)


@bp.route('/properties/<int:real_state_id>', methods=['DELETE'])
def delete_property(real_state_id):
    return PropertyController.delete_property(real_state_id)
