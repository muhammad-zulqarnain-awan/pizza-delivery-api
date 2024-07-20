from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):

    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, auto_increment=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, server_default="FALSE")
    is_staff = Column(Boolean, server_default="FALSE")

    orders = relationship('Order', back_populates=('users'))

    def __repr__(self) -> str:
        return f"<UserID: {self.user_id}, Username: {self.username}"
