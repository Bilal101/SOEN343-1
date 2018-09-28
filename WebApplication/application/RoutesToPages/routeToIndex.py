from flask import render_template
from application import app
import random 

@app.route('/')
@app.route('/index')
def index():
	course = 'SOEN343'
	books = [
		{
			'author':'randomly generated author ' + str(random.randint(0,100)) + '',
			'title': 'randomly generated book title ' + str(random.randint(0,100)) + ''

		},
		{
			'author':'randomly generated author ' + str(random.randint(0,100)) + '',
			'title': 'randomly generated book title ' + str(random.randint(0,100)) + ''
		},
		{
			'author':'randomly generated author ' + str(random.randint(0,100)) + '',
			'title': 'randomly generated book title ' + str(random.randint(0,100)) + ''
		}
	]

	return render_template('index.html', course='SOEN343', books=books)

