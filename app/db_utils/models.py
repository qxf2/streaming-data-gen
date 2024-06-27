"""
SQLAlchemy User model definition.

This script defines the User model for the database, including the columns and table name.
"""

from sqlalchemy import Column, Integer, String
from app.db_utils.database import Base


class User(Base):
    """
    User model for the SQLAlchemy ORM.

    Attributes:
        id (int): The primary key for the user.
        username (str): The unique username of the user.
        hashed_password (str): The hashed password of the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
