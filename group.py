from sqlalchemy import func
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
# group User by age
users = session.query(User.age).group_by(User.age).all()
print(users)
# SELECT age FROM User GROUP BY age
# [(14,), (15,), (16,), (17,), (18,), (19,), (20,), (25,), (29,)]
# group User by age and show the number for each age
users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(users)
# [(14, 5), (15, 6), (16, 1), (17, 2), (18, 1), (19, 2), (20, 3), (25, 1), (29, 1)]
