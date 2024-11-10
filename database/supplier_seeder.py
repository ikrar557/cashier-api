from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv(override=True)

db_driver = os.getenv("DB_DRIVER", "postgresql")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT", "5432")
db_database = os.getenv("DB_DATABASE")

if not all([db_driver, db_username, db_host, db_database, db_port]):
    raise ValueError("Missing required database configuration in environment variables")

db_url = f"{db_driver}://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}"

fake = Faker()

engine = create_engine(db_url)  # Use the correct db_url here
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

supplier = Table('supplier', metadata, autoload_with=engine)

def seed_data():
    for _ in range(10): 
        session.execute(
            supplier.insert().values(
                nama=fake.name(),
                alamat=fake.address(),
                nohp=fake.phone_number()
            )
        )
    session.commit()
    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
