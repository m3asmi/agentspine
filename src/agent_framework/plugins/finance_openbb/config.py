from pydantic import BaseModel, Field


class OpenBBProviderSettings(BaseModel):
    enabled: bool = False
    provider_id: str = "openbb"
    timeout_seconds: int = Field(default=20, ge=1, le=120)
    api_key_secret_ref: str | None = None
