from sqlalchemy import func
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User)
only_ulrich = True
group_by_age = True

if only_ulrich:
  users = users.filter(User.name == "Ulrich Stern")
if group_by_age:
  users = users.group_by(User.age)

users = users.all()

for user in users:
  print(f"Age: {user.age}: {user.name}")
# Age: 14: Ulrich Stern
# Age: 20: Ulrich Stern


users = session.query(User)
only_ulrich = False
group_by_age = True

if only_ulrich:
  users = users.filter(User.name == "Ulrich Stern")
if group_by_age:
  users = users.group_by(User.age)

users = users.all()

for user in users:
  print(f"Age: {user.age}: {user.name}")
# Age: 14: Odd denla
# Age: 15: Jeremy Belpon
# Age: 16: Clack Chan
# Age: 17: Hiroki Ishuyama
# Age: 18: Odd denla
# Age: 19: Clack Chan
# Age: 20: Odd denla
# Age: 25: New Name
# Age: 29: Calvin Long