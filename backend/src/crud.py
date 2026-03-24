from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import bcrypt
from . import models, schemas

def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

async def get_tenant_by_id(db: AsyncSession, tenant_id: int):
    result = await db.execute(select(models.Tenant).where(models.Tenant.id == tenant_id))
    return result.scalars().first()

async def get_tenant_by_domain(db: AsyncSession, domain: str):
    result = await db.execute(select(models.Tenant).where(models.Tenant.domain == domain))
    return result.scalars().first()

async def create_tenant(db: AsyncSession, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(name=tenant.name, domain=tenant.domain)
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        tenant_id=user.tenant_id,
        is_active=user.is_active,
        is_sena_admin=user.is_sena_admin
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
