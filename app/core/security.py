from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
import secrets

from app.config import API_KEY

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def verify_api_key(
    api_key: str | None = Security(api_key_header)
):

    if (
        not api_key
        or not API_KEY
        or not secrets.compare_digest(api_key, API_KEY)
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    return api_key
