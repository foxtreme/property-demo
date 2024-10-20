from pydantic import BaseModel, Field
from typing import Optional


class PropertySchema(BaseModel):
    real_state_id: Optional[int] = Field(default=None)
    address: str = Field(nullable=False)
    address: str = Field(nullable=False)
    type: str = Field(nullable=False)
    status: str = Field(nullable=False)
    zipcode: str = Field(nullable=False)
    city: str = Field(nullable=False)
    country: str = Field(nullable=False)

    class Config:
        from_attributes = True
