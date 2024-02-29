import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


# Create the SQLite database file
database_dir = os.path.join(os.getcwd(), "db")
app_database = os.path.join(database_dir, "pancar.db")

engine = create_engine("sqlite:///" + app_database, echo=True)

# Create a base class for declarative models
Base = declarative_base()
Base.metadata.create_all(engine)
# Create the tables in the database


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# # Insert a new user
new_user = User(id=12, name="John Doe", age=25)
session.add(new_user)
session.commit()

# # Query all users
# users = session.query(User).all()
# for user in users:
#     print(user.name, user.age)

# # Update a user
# user = session.query(User).filter_by(name="John Doe").first()
# user.age = 30
# session.commit()

# # Delete a user
# user = session.query(User).filter_by(name="John Doe").first()
# session.delete(user)
# session.commit()

# Close the session
session.close()
