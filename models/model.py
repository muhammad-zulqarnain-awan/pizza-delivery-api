from sqlalchemy import Column, Integer, Boolean,  String, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_staff = Column(Boolean, server_default="FALSE", nullable=True)
    is_active = Column(Boolean, server_default="FALSE", nullable=True)

    orders = relationship('Order', back_populates='users')

    def __repr__(self):
        return f"<User: {self.id}, {self.username}"


class Order(Base):

    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("IN-TRANSIT", "in-transit"),
        ("DELIVERED", "delivered")
    )

    PIZZA_SIZE = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE", "extra-large")
    )

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    size = Column(ChoiceType(choices=PIZZA_SIZE), nullable=False, server_default="SMALL")
    order_status = Column(ChoiceType(choices=ORDER_STATUS), nullable=False, server_default="PENDING")
    user_id = Column(Integer, ForeignKey("users.id"))

    users = relationship('User', back_populates='orders')

    def __repr__(self):
        return "<Order: {self.id}, {self.user_id}"
