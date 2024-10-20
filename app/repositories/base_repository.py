from app import db
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def save(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, entity_id):
        return db.session.query(self.model).get(entity_id)

    def get_all(self):
        return db.session.query(self.model).all()

    def update(self, entity):
        db.session.commit()
        return entity

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
