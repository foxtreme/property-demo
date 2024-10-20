from app.models.real_state_property import RealStateProperty
from app.schemas.property_schema import PropertySchema
from flask import jsonify
from app.repositories.property_repository import PropertyRepository


property_repository = PropertyRepository()


class PropertyController:
    @staticmethod
    def add_property(data):
        try:
            property_data = PropertySchema(**data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

        new_property = RealStateProperty(
            address=property_data.address,
            type=property_data.type,
            status=property_data.status,
            city=property_data.city,
            zipcode=property_data.zipcode,
            country=property_data.country
        )
        saved_property = property_repository.save(new_property)
        return PropertySchema.from_orm(saved_property).dict(), 201

    @staticmethod
    def get_properties():
        properties = property_repository.get_all()
        return [PropertySchema.from_orm(prop).dict() for prop in properties], 200

    @staticmethod
    def get_property(real_state_id):
        real_state_property = property_repository.get_by_id(real_state_id)
        if real_state_property:
            return PropertySchema.from_orm(real_state_property).dict(), 200
        return jsonify({"error": "Property not found"}), 404

    @staticmethod
    def update_property(real_state_id, data):
        real_state_property = property_repository.get_by_id(real_state_id)
        if not real_state_property:
            return jsonify({"error": "Property not found"}), 404
        try:
            property_data = PropertySchema(**data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        for key, value in property_data.dict(exclude_unset=True).items():
            setattr(real_state_property, key, value)
        updated_property = property_repository.update(real_state_property)
        return PropertySchema.from_orm(updated_property).dict(), 200

    @staticmethod
    def delete_property(real_state_id):
        real_state_property = property_repository.get_by_id(real_state_id)
        if not real_state_property:
            return jsonify({"error": "Property not found"}), 404
        property_repository.delete(real_state_property)
        return jsonify({"message": "Property deleted"}), 204

