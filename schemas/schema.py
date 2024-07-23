from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SignUpModel(BaseModel):
    
    username: str
    email: EmailStr
    password: str
    is_staff: Optional[bool] = Field(None)
    is_active: Optional[bool] = Field(None)

    class Config:

        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "JohnDoe",
                "email": "johndoe@example.com",
                "password": "password",
                "is_staff": False,
                "is_active": True,
            }
        }

class SignUpResponseModel(BaseModel):
    
    id: int
    username: str
    email: EmailStr
    is_staff: bool
    is_active: bool

    class Config:

        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "JohnDoe",
                "email": "johndoe@example.com",
                "is_staff": False,
                "is_active": True,
            }
        }

class LogInModel(BaseModel):

    email: EmailStr
    password: str

    class Config:

        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "johndoe@example.com",
                "password": "password"
            }
        }