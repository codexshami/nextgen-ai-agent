from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = 'sqlite:///./sql_app.db'  # Update this to your database URL

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Define the base class for declarative models
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a new session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
