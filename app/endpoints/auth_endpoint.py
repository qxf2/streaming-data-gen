"""
Module for defining FastAPI endpoints for user authentication and token generation.

Endpoints:
    /register: Endpoint for registering a new user.
    /token: Endpoint for logging in a user and generating a token.
"""

from datetime import timedelta
import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db_utils import crud
from app.db_utils.database import SessionLocal
from app.db_utils import schemas
from app.models.auth_model import Token
from app.db_utils.crud import verify_password, create_access_token


logger = logging.getLogger(__name__)

ACCESS_TOKEN_EXPIRY = 7

router = APIRouter()


def get_db():
    """
    Generator function that yields a SQLAlchemy SessionLocal instance.

    Yields:
        SessionLocal: A database session object that can be used within a context manager.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to creates a new user.

    Parameters:
        user (schemas.UserCreate): The user data including username and password
        db (Session, optional): The database session. Defaults to the result of `get_db()`.

    Returns:
        schemas.User : The newly created user object from the database.
    """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    new_user = crud.create_user(db=db, user=user)
    return new_user


def authenticate_user(username: str, password: str, db: Session):
    """
    Authenticates a user based on the provided username and password.

    Parameters:
        username (str): The username of the user to authenticate.
        password (str): The password of the user to authenticate.
        db (Session): The database session to query user information.

    Returns:
        db_user: The authenticated user if successful, False otherwise.
    """
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        logger.debug("No user found with username: %s", username)
        return False
    if not verify_password(password, db_user.hashed_password):
        logger.debug("Password verification failed for user: %s", username)
        return False
    logger.debug("User %s authenticated successfully", username)
    return db_user


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> Token:
    """
    Endpoint for logging in a user and generating an access token.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        Token: The access token with the username as the subject.
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    logger.debug("Login successful for username: %s", form_data.username)
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRY)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
