from pydantic import BaseModel, EmailStr, Field, constr

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8)

class AuthLogin(BaseModel):
    username_or_email: str
    password: str

class TokenPair(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = Field(..., description="seconds until expiry")
    refresh_token: str | None = None

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    roles: list[str] = []
