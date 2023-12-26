# pip install flask-mysqldb






# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request


import view
import config
import database

from flask_mysqldb import MySQL


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/meryem')
def hello_world():
    return 'ben meryem  World'

@app.route('/')
def homepage():
	return view.homePage()



@app.route('/search', methods=['GET'])
def search():
	filter = ''
	if request.method == 'GET':
		filter = request.args.get('filter', '')
		if filter == '':
			return 'Bos geldi xd'
		#name=ali
		sorgu = 'SELECT name FROM table where name=ali'
		#cursor = mysql.connection.cursor()
		return filter.upper()
		#cursor.execute(sorgu,(None,isim,yas))
		#return database.get(filter, mysql)
	
	return 'Burcak sal bizi'




# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()

