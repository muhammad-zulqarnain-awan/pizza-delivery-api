from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.model import User, Order


CONN_STR = "postgresql://postgres:Admin12345.@localhost/pizza-order-db"

engine = create_engine(CONN_STR)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
