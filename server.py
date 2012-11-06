from flask import Flask, render_template, request
from pymongo import Connection
import json

app = Flask(__name__)
connection = Connection()
db = connection.reflections
collection = db.words

@app.route('/')
def start():
	return render_template('index.html')

@app.route('/', methods = ['POST'])
	#create match_data to return as json object for display
	#match data contains [0] a list of your keywords and 
	#[1] a dict mapping your keywords to lists of people who share those words
def get_JSON():

	#print request

	match_data = []
	words_to_match_names = {}

	name = request.form['fname']
	print "post request is still happening"
	doc = collection.find_one({'name':name})
	my_keywords = doc['keywords'].keys()
	match_data.append(my_keywords)

	for keyword in my_keywords:
		match_names = []
		match_docs = collection.find({'keywords.'+keyword:{'$exists':True}})
		#.sort({keywords.keyword, DESCENDING)
		for match_doc in match_docs:
			if match_doc['name'] != name:
				match_names.append(match_doc['name'])

		words_to_match_names[keyword] = match_names

	match_data.append(words_to_match_names)
	# #return expects the html of a page. We don't know how to send our information to be manipulated by a js file
	return json.dumps(match_data)
	
if __name__ == '__main__':
	app.run(debug=True)


#[(kw1,[name1, name2]), (kw2, [name1, name2, name3])]


