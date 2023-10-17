from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
# 1
users = session.query(User).all()
print(users)
user1 = users[0]
print(user1.id)
print(user1.name)
print(user1.age)
# 2
user = session.query(User).filter_by(id=2).one_or_none()
print(user.id)
print(user.name)
print(user.age)
# 3
user = session.query(User).filter_by(age=25).first()
print(user.id)
print(user.name)
print(user.age)
