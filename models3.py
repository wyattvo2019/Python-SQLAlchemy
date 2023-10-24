from sqlalchemy import  Column, Integer, String,create_engine, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, sessionmaker, relationship


db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Non-mapped Method
class BaseModel3(Base):
  __abstract__ = True
  __allow_unmapped__ = True
  id = Column(Integer, primary_key = True)

class Address3(BaseModel3):
  __tablename__ = "addresses3"
  city = Column(String)
  state = Column(String)
  zip_code = Column(Integer)
  user_id: Mapped[int] = mapped_column(ForeignKey("users3.id"))
  user: Mapped["User3"] = relationship(back_populates="addresses3") 
  def __repr__(self):
    return f"<Address(id={self.id}, city='{self.city}')>"

class User3(BaseModel3):
  __tablename__ = "users3"
  name = Column(String)
  age = Column(Integer)
  addresses3: Mapped[list["Address3"]] = relationship()
  def __repr__(self):
    return f"<User(id={self.id}, username='{self.name}')>"
  
Base.metadata.create_all(engine)