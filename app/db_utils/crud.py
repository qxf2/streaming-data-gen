"""
This module provides utility functions for user authentication and token management.
"""

import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import logging
from typing import Union

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db_utils import models, schemas
from app.models.auth_model import TokenData


logger = logging.getLogger(__name__)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

load_dotenv()

# To generate SECRET_KEY run: openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """
    Verify if a plain password matches a hashed password.

    Args:
        plain_password (str): The plain password to be verified.
        hashed_password (str): The hashed password to be compared against.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    Generates a hash of the provided password using the password hashing context.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def get_user(db: Session, user_id: int):
    """
    Retrieves a user from the database based on the provided user_id.

    Args:
        db (Session): The database session.
        user_id (int): The unique identifier of the user to retrieve.

    Returns:
        User: The user corresponding to the provided user_id, or None if not found.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """
    Retrieves a user from the database based on the provided username.

    Args:
        db (Session): The database session.
        username (str): The username of the user to retrieve.

    Returns:
        User: The user corresponding to the provided username, or None if not found.
    """
    user = db.query(models.User).filter(models.User.username == username).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of users from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The maximum number of users to retrieve. Defaults to 100.

    Returns:
        list: A list of User objects representing the retrieved users.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Creates a new user in the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The user data to create.

    Returns:
        User: The newly created user in the database.
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    Creates an access token with the given data and optional expiration time.

    Args:
        data (dict): The data to be encoded into the token.
        expires_delta (Union[timedelta, None], optional): The expiration time of the token.
        If None, the token will expire after 7 days. Defaults to None.

    Returns:
        str: The encoded JWT access token.

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    """
    Verify the provided JWT token and return the username contained in the payload.

    Args:
        token (str, optional): The JWT token to be verified. 
        Defaults to the result of the `oauth2_scheme` dependency.

    Returns:
        TokenData: An object containing the username extracted from the token payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = TokenData(username=username)
    except InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    return token_data
