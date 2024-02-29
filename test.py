from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Create a SQLite database file
database_dir = os.path.join(os.getcwd(), "db")
app_database = os.path.join(database_dir, "pancar.db")

engine = create_engine("sqlite:///" + app_database, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Define a model class
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


# Create the table in the database
Base.metadata.create_all(engine)


# Create a new user
def create_new_user():
    new_user = User(name="Eray", email="cancelikeray@gmail.com")
    session.add(new_user)
    session.commit()
    session.close()


# Read all users
def read_users():
    users = session.query(User).all()
    for user in users:
        print(user.name, user.email)
    session.close()


# Update a user
def update_user():
    user = session.query(User).filter_by(name="Eray").first()
    user.email = "eraycancelik@hotmail.com"
    session.commit()
    session.refresh(user)
    session.close()


# Delete a user
def delete_user():
    user = session.query(User).filter_by(name="Eray").first()
    session.delete(user)
    session.commit()
    session.close()


# create_new_user()
delete_user()
