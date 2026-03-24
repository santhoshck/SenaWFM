import asyncio
import os
import sys
import getpass
from pydantic import ValidationError

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import AsyncSessionLocal
from src.crud import create_user, get_user_by_email
from src.schemas import UserCreate

async def create_sena_admin():
    from dotenv import load_dotenv
    load_dotenv()

    env = os.getenv("ENVIRONMENT", "DEVELOPMENT").upper()
    
    if env == "DEVELOPMENT":
        email = "admin@senawfm.com"
        password = "admin"
        print(f"Running in DEVELOPMENT mode. Using default admin credentials: {email} / {password}")
    else:
        print(f"Environment detected as {env}.")
        email = input("Enter new Sena Admin email: ").strip()
        password = getpass.getpass("Enter new Sena Admin password: ")
        confirm_password = getpass.getpass("Confirm password: ")
        
        if password != confirm_password:
            print("Passwords do not match!")
            sys.exit(1)
            
        if not email or not password:
            print("Email and password cannot be empty.")
            sys.exit(1)

    async with AsyncSessionLocal() as session:
        existing_user = await get_user_by_email(session, email)
        if existing_user:
            if existing_user.is_sena_admin:
                print(f"Sena Admin with email {email} already exists.")
            else:
                existing_user.is_sena_admin = True
                await session.commit()
                print(f"User with email {email} updated to be a Sena Admin.")
            return

        try:
            user_data = UserCreate(
                email=email,
                password=password,
                is_sena_admin=True,
                is_active=True,
                tenant_id=None
            )
            await create_user(session, user_data)
            print(f"Successfully created Sena Admin user: {email}")
        except ValidationError as e:
            print(f"Validation Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Database Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(create_sena_admin())
