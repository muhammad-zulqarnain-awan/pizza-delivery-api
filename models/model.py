from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, server_default="FALSE")
    is_staff = Column(Boolean, server_default="FALSE")

    orders = relationship('Order', back_populates='user')

    def __repr__(self) -> str:
        return f"<UserID: {self.user_id}, Username: {self.username}"


class Order(Base):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("IN-TRANSIT", "in-transit"),
        ("DELIVERED", "delivered"),
    )

    PIZZA_SIZE = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE", "extra-large")
    )

    __tablename__ = "Orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), server_default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE), server_default="SMALL")
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)

    user = relationship('User', back_populates='orders')

    def __repr__(self) -> str:
        return f"<OrderID: {self.order_id}, UserID: {self.user_id}"