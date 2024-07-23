from database import engine, Base
from models.model import User, Order

Base.metadata.create_all(engine)