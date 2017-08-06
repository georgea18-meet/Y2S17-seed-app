# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Country, City, Post, Continent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#import wikipedia
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


@app.route('/test')
def test_22():
	return render_template('test.html') 


@app.route('/countries/<int:continent>')
def flags_menu(continent):
	countries = session.query(Country).filter_by(continet=continent).all()
	c = session.query(Continent).filter_by(id=continent).first()
	return render_template('flagslist.html',countries = countries,continent=c)

@app.route('/add/<int:country>', methods=['GET','POST'])
def adding_form(country):
	if request.method =='GET':
		citie = session.query(City).filter_by(country=country).all()
		cities=[]
		for c in citie:
			cities.append(c.name)
		cities.sort()
		cities_l = []
		for cit in cities:
			ci = session.query(City).filter_by(name=cit).first()
			cities_l.append(ci)
		return render_template('add.html',cities=cities_l,country=country)
	else:
		post = Post()
		post.sender = request.form.get('name')
		post.text = request.form.get('review')
		post.sender_country = request.form.get('usercountry')
		post.city = request.form.get('city')
		post.country = country
		post.pic_url = request.form.get('img')
		session.add(post)
		session.commit()

		return redirect(url_for('country',country=country))

@app.route('/cities/<int:country>')
def country(country):
	continents = session.query(Continent).all()
	countr = session.query(Country).filter_by(id=country).first()
	cities = session.query(City).filter_by(country=country).all()
	all_cities = session.query(City).all()
	posts = session.query(Post).filter_by(country=country).all()
	posts.reverse()
	if countr.name=='Georgia':
		info = wikipedia.page(countr.name+' country').content.split('==')
	else:
		info = wikipedia.page(countr.name).content.split('==')
	return render_template('country_feed.html',cities=cities,country=countr,info=info,continents=continents,posts=posts,acities=all_cities)

@app.route('/cities/list/<int:country>',methods=['GET','POST'])
def cities_list(country):
	countr = session.query(Country).filter_by(id=country).first()
	if request.method=='GET':
		citie = session.query(City).filter_by(country=country).all()
	else:
		val = str(request.form.get('Search'))
		citi = session.query(City).filter_by(country=country).all()
		citie = []
		for b in citi:
			if str(b.name).upper().startswith(val.upper()):
				citie.append(b)
	cities=[]
	for c in citie:
		cities.append(c.name)
	cities.sort()
	cities_l = []
	for cit in cities:
		ci = session.query(City).filter_by(name=cit).first()
		cities_l.append(ci)
	lenn=len(cities)
	return render_template('cities_list.html',cities=cities_l,country=countr)	

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
		c.continet = request.form.get('continent')
		c.flag = request.form.get('flag')
		session.commit()
		return redirect(url_for('addinfo',country=country))

@app.route('/test')
def test():
	countries = session.query(Country).all()
	cities = session.query(City).all()
	posts = session.query(Post).all()
	return render_template('database_test.html',countries=countries,cities=cities,posts=posts)
