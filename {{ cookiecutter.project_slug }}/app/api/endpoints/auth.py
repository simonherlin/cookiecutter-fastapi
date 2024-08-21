from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.core.security import verify_password, create_access_token
from app.schemas.token import Token
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.utils.dependency import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
