from fastapi import Header, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import get_db
from .models import Tenant
from . import crud

async def get_tenant_header(x_tenant_id: str = Header(..., description="The unique domain or ID of the tenant"), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant).where(Tenant.domain == x_tenant_id))
    tenant = result.scalars().first()
    if not tenant:
        raise HTTPException(status_code=400, detail="Invalid tenant header")
    return tenant

async def is_current_user_sena_admin(
    x_user_email: str = Header(..., description="The email of the Sena Admin"),
    db: AsyncSession = Depends(get_db)
):
    user = await crud.get_user_by_email(db, email=x_user_email)
    if not user or not user.is_sena_admin:
        raise HTTPException(status_code=403, detail="Not authorized. Sena Admin privileges required.")
    return user
