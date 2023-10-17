from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

class Person(Base):
  __tablename__ = "people"

  ssn =Column("ssn", Integer, primary_key=True)
  firstname = Column("firstname", String)
  lastname = Column("lastname", String)
  gender = Column("gender", CHAR)
  age = Column("age", Integer)

  def __init__(self, ssn, first, last, gender, age):
    self.ssn = ssn
    self.fistname = first
    self.lastname = last
    self.gender = gender
    self.age = age
  def __repr__(self):
    return f"({self.ssn} {self.fistname} {self.lastname} {self.gender} {self.age})"

Base.metadata.create_all(engine)
