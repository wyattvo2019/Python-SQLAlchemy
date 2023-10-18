from models import User, engine
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=engine)
session = Session()

# order all user by ages ascending
users = session.query(User).order_by(User.age).all()
for user in users:
  print(f"User age: {user.age}, name: {user.name}, id: {user.id}")
# order all user by ages ascending
users = session.query(User).order_by(User.age.desc()).all()
for user in users:
  print(f"User age: {user.age}, name: {user.name}, id: {user.id}")
# order all user by ages, names
users = session.query(User).order_by(User.age, User.name).all()
for user in users:
  print(f"User age: {user.age}, name: {user.name}, id: {user.id}")


