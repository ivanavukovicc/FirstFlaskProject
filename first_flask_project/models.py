from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Izdavac(Base):
    __tablename__ = 'izdavac'

    id = Column(Integer, primary_key=True)
    ime = Column(String, nullable=False)
    adresa = Column(String)
    telefon = Column(String)

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    autor = Column(String)


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)