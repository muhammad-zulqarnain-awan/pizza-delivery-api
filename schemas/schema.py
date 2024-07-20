from pydantic import BaseModel, EmailStr
from typing import Optional

class SignUpModel(BaseModel):

    id: Optional[int]
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool]
    is_staff: Optional [bool]

    class Config:

        from_attributes = True
        json_schema_extra = {
            'example': {
                'username': 'John Doe',
                'email': 'johndoe@example.com',
                'password': 'password',
                'is_active': False,
                'is_staff': True
            }
        }

