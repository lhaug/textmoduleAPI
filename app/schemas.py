from datetime import datetime
from pydantic import BaseModel

class TextmoduleBase(BaseModel):
    title: str
    content: str

class TextmoduleCreate(TextmoduleBase):
    pass

class TextmoduleOut(TextmoduleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True