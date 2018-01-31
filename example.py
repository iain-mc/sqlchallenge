import flask
import werkzeug
import jinja2
import sqlite3

from flask import Flask
from flask import render_template
from flask import request
from flask import g

DATABASE = './users.db'

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row    
    return db

def rows_to_string(rows):
	res = ""
	for row in rows:
		for key in row.keys():
			res += row[key] + ','
		res += '\n'
	return res

app = Flask(__name__)

@app.route('/index', methods=['POST','GET'])
def index():
	if(request.method == 'GET'):
		return render_template('index.html')
	if(request.method == 'POST'):
		if(request.form['user']):
				user = request.form['user']
				query = 'select interests from users where name = "' + user + '" and isRestricted = 0'
				print query
				usertable = query_db(query, (), one=False)
				result = rows_to_string(usertable)
				return render_template('index.html', interests = result)
	
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if(__name__ == '__main__'):
	app.run(host='0.0.0.0', port=5000, debug=True)
