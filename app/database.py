from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:admin1234@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)
print(type(settings.database_password))
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine
)

Base = declarative_base() 

 
def get_db(): 
    db = SessionLocal()
 
    try:
        yield db
    
    finally:
        db.close()