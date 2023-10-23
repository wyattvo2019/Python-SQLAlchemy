from sqlalchemy import func
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# chaining
users_tuple = (
  session.query(User.age, func.count(User.id))
  .filter(User.age > 10)
  .group_by(User.age)
  .filter(User.age < 20)
  .group_by(User.age)
  .all()
)
# SELECT age, COUNT(id)
# FROM users
# WHERE age > 10 AND age <20
# GROUP BY age
# ORDER BY "age"
for age, count in users_tuple:
  print(f"Age: {age}: {count} users")
# Age: 14: 5 users
# Age: 15: 6 users
# Age: 16: 1 users
# Age: 17: 2 users
# Age: 18: 1 users
# Age: 19: 2 users
