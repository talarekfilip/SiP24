# database.py
from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import urllib.parse

# Load environment variables
load_dotenv()

# Kodowanie znaków specjalnych w haśle
password = urllib.parse.quote_plus("zaq1@WSX")

# Database URL - Using environment variable or default
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    f"postgresql://postgres:{password}@localhost/sip24db"
)

# Create SQLAlchemy engine with client encoding and other connection parameters
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True,
    connect_args={
        'client_encoding': 'utf8',
        'options': '-c timezone=UTC -c lc_messages=pl_PL.UTF-8'
    }
)

# Set UTF-8 encoding for all connections
@event.listens_for(engine, "connect")
def set_utf8(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET client_encoding='UTF8';")
    cursor.execute("SET timezone='UTC';")
    cursor.execute("SET lc_messages TO 'pl_PL.UTF-8';") 
    cursor.execute("SET lc_monetary TO 'pl_PL.UTF-8';")
    cursor.execute("SET lc_numeric TO 'pl_PL.UTF-8';")
    cursor.execute("SET lc_time TO 'pl_PL.UTF-8';")
    cursor.close()

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 