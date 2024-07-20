from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


CONN_STR = "postgresql://postgres:Admin12345.@localhost/pizza-ordering-db"

engine = create_engine(CONN_STR)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()