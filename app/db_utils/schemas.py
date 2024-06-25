"""
Pydantic models for User operations.

This script defines the Pydantic models used for user-related operations.
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base model for user information.

    Attributes:
        username (str): The username of the user.
    """

    username: str


class UserCreate(UserBase):
    """
    Model for creating a new user.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
    """

    password: str


class User(UserBase):
    """
    Complete user model with ID.

    Attributes:
        username (str): The username of the user.
        id (int): The unique identifier of the user.
    """

    id: int

    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        from_attributes = True
