import jwt
import datetime

from ..config import settings
from ..models.user import User


def generate_token(data: User, expiry_time_delta: int):
    data = {
        "sub": data["_id"],
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=expiry_time_delta),
        "iat": datetime.datetime.utcnow(),
    }
    return jwt.encode(
        payload=data, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
