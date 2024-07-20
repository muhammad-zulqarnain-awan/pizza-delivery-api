from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base

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

    order_id = Column(Integer, primary_key=True, auto_increment=True)
    quantity = Column(Integer, nullable=False, unique=True)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), server_default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE), server_default="SMALL")
    user_id = Column(Integer, ForeignKey('users.user_id'))

    order = relationship('User', back_populates='orders')

    def __repr__(self) -> str:
        return f"<Order: {self.order_id}, UserID: {self.user_id}"
