from fastapi import APIRouter, status, HTTPException
from models.model import User
from schemas.schema import SignUpModel, SignUpResponseModel
from werkzeug.security import generate_password_hash
from database import SessionLocal, engine

session = SessionLocal(bind=engine)

auth_route = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_route.get("/")
def root():
    return {"message": "Auth Routes"}


@auth_route.post("/signup", response_model=SignUpResponseModel, status_code=status.HTTP_201_CREATED)
def signup(signupuser: SignUpModel, ):

    db_email = session.query(User).filter(User.email == signupuser.email).first()
    db_username = session.query(User).filter(User.username == signupuser.username).first()

    if  db_email or db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists!")

    signupuser.password = generate_password_hash(signupuser.password)
    
    newuser = User(**signupuser.model_dump())

    session.add(newuser)
    session.commit()

    return newuser
