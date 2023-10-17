from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
user = User(name="John Doe", age=30)
user2 = User(name="Lily Smith", age=25)
user3 = User(name="Calvin Long", age=29)
session .add(user)
session.add_all([user2, user3])
session.commit()