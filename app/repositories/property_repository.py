from app.models.real_state_property import RealStateProperty
from app.repositories.base_repository import BaseRepository


class PropertyRepository(BaseRepository):
    def __init__(self):
        super().__init__(RealStateProperty)
