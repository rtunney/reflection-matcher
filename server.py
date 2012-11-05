from flask import Flask, render_template, request
from pymongo import Connection
import json

app = Flask(__name__)
connection = Connection()
db = connection.reflections
theData = db.words

@app.route('/', methods=['GET', 'POST'])
def start():
	if request.method=='GET':
		return render_template('index.html')

	elif request.method=='POST':
		name = request.form['fname']
		doc = theData.find_one({'name':name})
		keywords = doc['keywords']
		#return expects the html of a page. We don't know how to send our information to be manipulated by a js file
		return json.dumps(keywords)
	
if __name__ == '__main__':
	app.run(debug=True)


#[(kw1,[name1, name2]), (kw2, [name1, name2, name3])]


