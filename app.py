from flask import Flask, render_template, url_for, request
# import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.database = "sample.db" # added in database video Part 5
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #added part 9
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True

#create SQLALCHEMY object
db = SQLAlchemy(app)

from models import *

# #added in database video part 5
# def connect_db():
# 	return sqlite3.connect(app.database)

@app.route('/')
def home():
	#return "Hello World"
	# in this case g is our connection object
	# g.db = connect_db() #g is an imported thing in python? g is an object specific for flask, used to store a temerarry object
	# cur = g.db.execute('select * from posts') #cursor 
	# # no cast the returnd db query to a dictionary 
	# posts = [dict(title = row[0], description = row[1]) for row in cur.fetchall()]
	# g.db.close()
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST']) #applying methods to a route
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



if __name__== '__main__':
	app.run(debug=True)


