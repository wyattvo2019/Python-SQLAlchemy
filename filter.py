from models import User, engine
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy import or_

Session = sessionmaker(bind=engine)
session = Session()

# ==========query all user with age greater than or equal 25
# ==query all users
# users = session.query(User).all()
# user_filtered = session.query(User).filter(User.age >= 25).all()
# print("All users:", len(users))
# print("Users >= 25 :", len(user_filtered))

# ===========query user with age is 20
# users = session.query(User).filter_by(age = 20).all()
# for user in users:
#   print(f"{user.id}, {user.age}")

# ===========query user with age >= 20 OR name is Ulrich Stern
users = session.query(User).where(or_(User.age >= 20, User.name=="Ulrich Stern")).all()
for user in users:
  print(f"{user.age}, {user.name}")




