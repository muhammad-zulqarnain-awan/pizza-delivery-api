from fastapi import APIRouter, status, HTTPException
from werkzeug.security import generate_password_hash
from database import SessionLocal
from schemas.schema import SignUpModel
from models.model import User


auth_router = APIRouter(
    prefix="/auth",
    tags=['Auth']
)

session = SessionLocal()

@auth_router.get("/")
def root():
    return {"message": "Auth Router"}

@auth_router.post("/signup", response_model=SignUpModel, status_code=status.HTTP_201_CREATED)
def signup(signup_user: SignUpModel):
    
    db_email = session.query(User).filter(User.email == signup_user.email).first()
    db_username = session.query(User).filter(User.username == signup_user.username).first()

    if not db_email or db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or Email Address already exists!")
    
    new_user = User(
        username=signup_user.username,
        email=signup_user.email,
        password=generate_password_hash(signup_user.password),
        is_active=signup_user.is_active,
        is_staff=signup_user.is_staff
    )

    session.add(new_user)
    session.commit()

    return {"message": "Sign UP successfully"}



@auth_router.post("/login")
def login():
    pass

