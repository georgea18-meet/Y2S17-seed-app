from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import pycountry

Base = declarative_base()

class Continet(Base):
    __tablename__  = 'continent'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # ADD YOUR FIELD BELOW ID
class Country(Base):
	__tablename__ = 'country'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	continet = Column(Integer)#continent id
	population = Column(Integer)

class City(Base):
	__tablename__ = 'city'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	country = Column(Integer)#country id
	capital = Column(Boolean, default=False)

class Posts(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	sender = Column(String)
	text = Column(String)
	sender_country = Column(Integer)
	city = Column(Integer)#city id
	country = Column(Integer)#country id
	pic_url = Column(String(140))

