from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Textmodule(Base):
    __tablename__ = "textmodules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False, index=True)
    content = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)