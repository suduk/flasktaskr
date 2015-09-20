from flask import Flask, flash, redirect, session, render_template, url_for, request
import sqlite3
from functools import wraps


app=Flask(__name__)
app.config.from_object('_config')


#helper function
def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		if session.get('logged_in'):
			if session['loggedin']:
				return f(*args,**kwargs)
			else:
				flash('You have to login')
				return redirect(url_for('login'))
	return wrapper


@app.route('/logout')
def logout():
	if session.get('logged_in'):
		session.pop('logged_in')
		flash('Goodby')
		return redirect(url_for('login'))



@app.route('/',methods=['POST','GET'])
def login():
	error=None
	print request.method
	if request.method=='POST':
		if request.form['username']!=app.config['USERNAME'] or \
			request.form['password']!=app.config['PASSWORD']:
			error='wrong pass or username'
			print error
			render_template('login.html',error=error)
		else:
			print "good pass and login"
			session['logged_in']=True
			flash('you have logged in')
			return redirect(url_for('tasks'))

	return render_template('login.html',error=error)		

@app.route('/tasks')
def tasks():
	print 'inside tasks'
	return render_template('tasks.html')