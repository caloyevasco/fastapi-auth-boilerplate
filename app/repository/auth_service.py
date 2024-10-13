from fastapi import HTTPException

from ..models.auth import LoginCredentials
from ..models.auth import AuthResponse
from ..models.user import User

from ..database import users_collection
from ..api_utils.token_helper import generate_token
from ..config import settings


async def auth_if_user_exists(data: LoginCredentials) -> AuthResponse | dict:
    document = await users_collection.find_one(data.model_dump())
    document["_id"] = str(document["_id"])
    if document:
        return AuthResponse(
            status="success",
            access_token=generate_token(
                document, expiry_time_delta=settings.ACCESS_TOKEN_DURATION
            ),
            refresh_token=generate_token(
                document, expiry_time_delta=settings.REFRESH_TOKEN_DURATION
            ),
        )
    raise HTTPException(status_code=401, detail="Unauthorized")


async def find_user(query: dict) -> dict:
    return await users_collection.find_one(query)
