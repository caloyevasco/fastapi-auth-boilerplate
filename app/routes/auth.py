from fastapi import APIRouter

from ..repository.auth_service import auth_if_user_exists
from ..models.auth import LoginCredentials
from ..models.auth import AuthResponse

auth_router = APIRouter()


@auth_router.post("/login", response_model=AuthResponse | dict)
async def login(data: LoginCredentials):
    return await auth_if_user_exists(data)
