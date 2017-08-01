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

cl = []
for b in list(pycountry.countries):
	cl.append(str(b.alpha_2))
gc = geonamescache.GeonamesCache()
gcd = gc.get_cities()
for k in gcd.keys():
	city = City()
	city.name = str(gcd[k][u'name'])
	al2 = str(gcd[k][u'countrycode'])
	if cl.count(al2)>0:
		ind = cl.index(al2)
		cn = session.query(Country).filter_by(name=list(pycountry.countries)[ind].name).first().id
		city.country = cn
		session.add(city)
	else:
		print('HAPPY BIRTHDAY!!!')
session.commit()