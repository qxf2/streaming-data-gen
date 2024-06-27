from pydantic import BaseModel
from typing import Union

class Token(BaseModel):
    """
    Pydantic model representing a token.

    Attributes:
        access_token (str): The access token.
        token_type (str): The type of the token.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Pydantic model representing token data.

    Attributes:
        username (Union[str, None]): The username associated with the token,
            or None if the token is not associated with any user.
    """
    username: Union[str, None] = None

