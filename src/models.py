import os

from sqlalchemy import create_engine, Integer, String,  Column
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# * Fetch environment variables
db_driver = os.getenv("DB_DRIVER", "postgresql")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")
db_port = os.getenv("DB_PORT", "5432")

# * Check if any required environment variable is missing
if not all([db_driver, db_username, db_host, db_database, db_port]):
    raise ValueError("Missing required database configuration in environment variables")

url = URL.create(
    drivername=db_driver,
    username=db_username,
    password=db_password,
    host=db_host,
    database=db_database,
    port=int(db_port),
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Items(Base):
    __tablename__ = "barang"
    
    nobarcode = Column(Integer, primary_key=True)
    nama = Column(String)
    harga = Column(Integer)
    stok = Column(Integer)
    
class Supplier(Base):
    __tablename__ = "supplier"
    
    idsup = Column(Integer, primary_key=True)
    nama = Column(String, index=True)
    alamat = Column(String)
    nohp = Column(String)