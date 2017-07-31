from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import pycountry
from model import Base, Country, City, Post, Continent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
import pycountry
my_countries = list(pycountry.countries)
for i in my_countries:
	country = Country()
	country.name = i.name
	session.add(country)

continents = ['Europe','Africa','Asia','North America','South America','Australia']
for i in continents:
	con = Continent()
	con.name = i
	session.add(con)
session.commit()