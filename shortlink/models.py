from sqlalchemy import Column, String, Integer

from .database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, unique=True)
    target_url = Column(String, index=True)
    key = Column(String, unique=True, index=True)
    