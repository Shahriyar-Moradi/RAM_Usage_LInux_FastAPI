

from database import Base
from sqlalchemy import Column, Integer, String, Float


class MemoryItem(Base):
    __tablename__ = "Memory"
    id = Column(Integer, primary_key=True)
    total = Column(Float)
    used = Column(Float)
    free = Column(Float)
