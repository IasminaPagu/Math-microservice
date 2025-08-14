from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import UserCreate, AuthLogin, TokenPair, UserOut
from app.models.db_models import User, Role
from app.utils.security import (get_db, hash_password, verify_password,
                                create_token, ACCESS_MIN, REFRESH_DAYS)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == payload.username) | (User.email == payload.email)).first():
        raise HTTPException(status_code=409, detail="Username or email exists")
    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.flush() 

    role_user = db.query(Role).filter(Role.name == "user").first() 
    if role_user is None: 
        role_user = Role(name="user"); db.add(role_user); db.flush()

    user.roles.append(role_user)
    db.commit(); db.refresh(user)

    return UserOut(
        id=user.id, username=user.username, email=user.email,
        roles=[r.name for r in user.roles]
    )

@router.post("/login", response_model=TokenPair)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    identifier = form.username
    password = form.password
    user = db.query(User).filter(
        (User.username == identifier) | (User.email == identifier)
    ).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Bad credentials")

    access = create_token(user.username, minutes=ACCESS_MIN)
    return {"access_token": access, "expires_in": ACCESS_MIN*60, "token_type": "bearer"}


@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == payload.username) | (User.email == payload.email)).first():
        raise HTTPException(status_code=409, detail="Username or email exists")
    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.flush() 

    role_user = db.query(Role).filter(Role.name == "user").first()
    if role_user is None:
        role_user = Role(name="user"); db.add(role_user); db.flush()

    user.roles.append(role_user)
    db.commit(); db.refresh(user)

    return UserOut(
        id=user.id, username=user.username, email=user.email,
        roles=[r.name for r in user.roles]
    )

