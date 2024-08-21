from fastapi import FastAPI
from app.api.v1.endpoints import auth, users, items
from app.db import base  # Import models
from app.db.session import engine

app = FastAPI()

base.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
