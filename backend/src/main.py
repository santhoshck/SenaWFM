from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import admin, auth

app = FastAPI(title="SenaWFM API", version="0.1.0")

app.include_router(admin.router)
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the SenaWFM API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
