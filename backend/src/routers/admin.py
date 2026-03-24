from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .. import crud, schemas, models
from ..database import get_db
from ..dependencies import is_current_user_sena_admin

router = APIRouter(
    prefix="/api/admin",
    tags=["admin"],
    dependencies=[Depends(is_current_user_sena_admin)],
)

@router.post("/tenants", response_model=schemas.TenantResponse)
async def create_new_tenant(tenant: schemas.TenantCreate, db: AsyncSession = Depends(get_db)):
    db_tenant = await crud.get_tenant_by_domain(db, domain=tenant.domain)
    if db_tenant:
        raise HTTPException(status_code=400, detail="Tenant domain already registered")
    return await crud.create_tenant(db=db, tenant=tenant)

@router.post("/users", response_model=schemas.UserResponse)
async def create_new_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if user.tenant_id is not None:
        db_tenant = await crud.get_tenant_by_id(db, tenant_id=user.tenant_id)
        if not db_tenant:
            raise HTTPException(status_code=400, detail="Tenant not found")

    return await crud.create_user(db=db, user=user)
