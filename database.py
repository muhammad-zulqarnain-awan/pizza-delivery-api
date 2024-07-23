from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:Admin12345.@localhost/pizza-deliver-app-db")

Base = declarative_base()

SessionLocal = sessionmaker()