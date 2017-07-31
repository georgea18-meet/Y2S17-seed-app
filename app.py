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
def hello_world():
    return render_template('index.html')

@app.route('/countries/<int:continent>')
def flags_menu(continent):
	countries = session.query(Country).filter_by(continent=continent).all()
    return render_template('flagslist.html',countries = countries,continent=continent)

@app.route('/add/<str:country>', methods=['GET','POST'])
def adding_form(country):
	if request.method()=='GET':
		cities = session.query(City).filter_by(country=country).all()
		return render_template('add.html',cities=cities)
	else:
		post = Post()
		post.sender = request.form.get(name)
		post.text = request.form.get(review)
		post.sender_country = request.form.get(usercountry)
		post.city = request.form.get(city)
		post.country = session.query(City).filter_by(id=post.city).first().country
		post.pic_url

		return redirect(url_for('feed',country=country))

@app.route('/cities/<str:country>')
def country(country):
	cities = session.query(City).filter_by(country=country).all()
	return render_template('country.html',cities=cities,country=country)

@app.route('/feed/<str:city>')
def feed(city):
	posts = session.query(Post).filter_by(city=city).all()
	return render_template('cityfeed.html'.posts=posts,city=city)