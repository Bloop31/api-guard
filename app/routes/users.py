from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.schemas import UserCreate, UserLogin, Token
from app.auth import hash_password, verify_password, create_access_token, verify_token
from app.database import get_db
from app.models import User

router=APIRouter()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
def get_current_user(token: str=Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_email = payload.get("sub")
    user = db.query(User).filter(User.email==user_email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": user.email}