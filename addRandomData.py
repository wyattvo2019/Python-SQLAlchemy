from models import User, engine
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=engine)
session = Session()

names = ["Joe Bin", "Clack Chan", "Hiroki Ishuyama", "Odd denla", "Ulrich Stern", "Jeremy Belpon", "Aelita Stone"]
ages = [14, 15, 16, 17, 18, 19, 20]
for x in range(20):
  user = User(name=random.choice(names), age=random.choice(ages))
  session.add(user)
session.commit()

