import asyncio
from src.database import AsyncSessionLocal
from src.crud import get_user_by_email, verify_password
from src.routers.auth import create_access_token
from datetime import timedelta

async def test():
    async with AsyncSessionLocal() as db:
        user = await get_user_by_email(db, "admin@senawfm.com")
        print("User:", user)
        res = verify_password("admin", user.hashed_password)
        print("verify_password:", res)
        
        access_token_expires = timedelta(minutes=60*24)
        access_token = create_access_token(
            data={"sub": str(user.email), "tenant_id": user.tenant_id, "is_admin": user.is_sena_admin},
            expires_delta=access_token_expires
        )
        print("Token:", access_token)

try:
    asyncio.run(test())
except Exception as e:
    import traceback
    traceback.print_exc()
