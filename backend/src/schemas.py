from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class TenantBase(BaseModel):
    name: str
    domain: str

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_sena_admin: bool = False

class UserCreate(UserBase):
    password: str
    tenant_id: Optional[int] = None

class UserResponse(UserBase):
    id: int
    tenant_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True
