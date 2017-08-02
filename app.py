# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Country, City, Post, Continent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def main():
    return render_template('mainpage.html')


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/Q&A')
def Q_A():
	return render_template('Q&A.html')    


@app.route('/countries/<int:continent>')
def flags_menu(continent):
	countries = session.query(Country).filter_by(continet=continent).all()
	c = session.query(Continent).filter_by(id=continent).first()
	return render_template('flagslist.html',countries = countries,continent=c)

@app.route('/add/<int:country>', methods=['GET','POST'])
def adding_form(country):
	if request.method =='GET':
		cities = session.query(City).filter_by(country=country).all()
		return render_template('add.html',cities=cities)
	else:
		post = Post()
		post.sender = request.form.get('name')
		post.text = request.form.get('review')
		post.sender_country = request.form.get('usercountry')
		post.city = request.form.get('city')
		post.country = session.query(City).filter_by(id=post.city).first().country
		post.pic_url

		return redirect(url_for('feed',country=country))

@app.route('/cities/<int:country>')
def country(country):
	cities = session.query(City).filter_by(country=country).all()
	return render_template('country.html',cities=cities,country=country)

@app.route('/feed/<int:city>')
def feed(city):
	posts = session.query(Post).filter_by(city=city).all()
	return render_template('cityfeed.html',posts=posts,city=city)

@app.route('/addinfo/<int:country>',methods=['GET','POST'])
def addinfo(country):
	c = session.query(Country).filter_by(id=country).first()
	continents = session.query(Continent).all()
	if request.method == 'GET':
		return render_template('addinfo.html',country=c,continents=continents)
	else:
<<<<<<< HEAD
		c.continent = request.form.get('continent')
=======
		c.continet = request.form.get('continent')
>>>>>>> 236a25570853b5cb21bb03347fd61ad3135c5fd7
		c.flag = request.form.get('flag')
		session.commit()
		return redirect(url_for('addinfo',country=country))

@app.route('/test')
def test():
	countries = session.query(Country).all()
	cities = session.query(City).all()
	return render_template('database_test.html',countries=countries,cities=cities)
