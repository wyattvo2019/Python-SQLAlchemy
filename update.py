from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

user = session.query(User).filter_by(id=1).one_or_none()
print(user.id)
print(user.name)
print(user.age)
user.name = "New Name"
print(user.name)
session.commit()
