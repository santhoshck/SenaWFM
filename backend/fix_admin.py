import asyncio
from src.database import AsyncSessionLocal
from src.crud import get_user_by_email, get_password_hash

async def fix():
    async with AsyncSessionLocal() as session:
        user = await get_user_by_email(session, "admin@senawfm.com")
        if user:
            user.hashed_password = get_password_hash("admin")
            await session.commit()
            print("Password updated to 'admin'")
        else:
            print("User not found")

asyncio.run(fix())
