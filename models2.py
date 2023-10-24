from sqlalchemy import  Column, Integer, String,create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Non-mapped Method
class BaseModel2(Base):
  __abstract__ = True
  __allow_unmapped__ = True
  id = Column(Integer, primary_key = True)

class Address2(BaseModel2):
  __tablename__ = "addresses2"
  city = Column(String)
  state = Column(String)
  zip_code = Column(Integer)
  user_id = Column(ForeignKey("users2.id"))
  user = relationship("User2", back_populates="addresses2") 
  def __repr__(self):
    return f"<Address(id={self.id}, city='{self.city}')>"

class User2(BaseModel2):
  __tablename__ = "users2"
  name = Column(String)
  age = Column(Integer)
  addresses2 = relationship(Address2)
  def __repr__(self):
    return f"<User(id={self.id}, username='{self.name}')>"
  
Base.metadata.create_all(engine)