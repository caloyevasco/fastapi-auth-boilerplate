from pydantic import BaseModel, Field


class LoginCredentials(BaseModel):
    email: str = Field(strict=True)
    password: str = Field(strict=True)


class AuthResponse(BaseModel):
    status: str
    access_token: str
    refresh_token: str
