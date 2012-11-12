from flask import Flask, render_template, request
from pymongo import Connection
import json
import os

app = Flask(__name__)
connection = Connection()
db = connection.reflections
collection = db.words

@app.route('/')
def start():
	return render_template('index.html')

@app.route('/favicon.ico')
def get_icon():
	return

@app.route('/<name>', methods=["GET"])
	#create match_data to return as json object for display

	#d3 template expects a dictionary with 2 key value pairs:
	#'name':name of node and 'children':list of child nodes 

	#child nodes are written as dictionaries identical to the one
	#described above.

def get_JSON(name):

	print "got request for " + name
	
	match_data = {}

	match_data['name'] = name
	match_data['children'] = []

	doc = collection.find_one({'name':name})
	print "name: " + name
	my_keywords = doc['keywords'].keys()

	for keyword in my_keywords:
		word_data = {}
		word_data['name'] = keyword
		word_data['children'] = []

		match_names = []
		match_docs = collection.find({'keywords.'+keyword:{'$exists':True}}).sort('keywords.'+keyword, -1)
	
		for match_doc in match_docs[:10]:
			if match_doc['name'] != name:
				match_names.append(match_doc['name'])

		for person in match_names:
			# INCLUDE TO CONCEAL LAST NAMES
			# space1 = person.find(" ")
			# space2 = person.find(" ", space1+1)

			person_data = {}
			num_kw_matches = collection.find_one({'name':person})['keywords'][keyword]
			person_data['name'] = (person
			# INCLUDE TO CONCEAL LAST NAMES
			# [:space1] 
			+ " (" + str(num_kw_matches) + ")" )
			word_data['children'].append(person_data)

		match_data['children'].append(word_data)

	return json.dumps(match_data)
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


