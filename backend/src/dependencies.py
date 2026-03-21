from fastapi import Header, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import get_db
from .models import Tenant

async def get_tenant_header(x_tenant_id: str = Header(..., description="The unique domain or ID of the tenant"), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant).where(Tenant.domain == x_tenant_id))
    tenant = result.scalars().first()
    if not tenant:
        raise HTTPException(status_code=400, detail="Invalid tenant header")
    return tenant
