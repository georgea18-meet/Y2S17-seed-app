from model import Base, Country, City, Post, Continent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import pycountry
import geonamescache
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

g = session.query(Post).filter_by(country=60).all()
g[6].country=61
session.commit()
session.query(Post).filter_by(country=61).delete()
session.commit()
