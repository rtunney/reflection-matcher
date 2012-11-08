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

@app.route('/<name>', methods=["GET"])
	#create match_data to return as json object for display
	#match data contains [0] a list of your keywords and 
	#[1] a dict mapping your keywords to lists of people who share those words
def get_JSON(name):

	#print request
	print "got request for " + name
	#name = request.form['fname']
	doc = collection.find_one({'name':name})
	my_keywords = doc['keywords'].keys()

	words_to_match_names = {}
	for keyword in my_keywords:
		match_names = []
		match_docs = collection.find({'keywords.'+keyword:{'$exists':True}}).sort('keywords.'+keyword, -1)
		#.sort({keywords.keyword, DESCENDING)
		for match_doc in match_docs:
			if match_doc['name'] != name:
				match_names.append(match_doc['name'])

		words_to_match_names[keyword] = match_names
	#-------------------------------------------
	#   OLD STUFF ABOVE, NEW STUFF BELOW. MERGE
	#-------------------------------------------
	match_data = {}

	match_data['name'] = name
	match_data['children'] = []

	for keyword in my_keywords:
		word_data = {}
		word_data['name'] = keyword
		word_data['children'] = []
		for person in words_to_match_names[keyword]:
			person_data = {}
			person_data['name'] = person
			word_data['children'].append(person_data)
		match_data['children'].append(word_data)

	return json.dumps(match_data)
	
if __name__ == '__main__':
	app.run(debug=True)


#[(kw1,[name1, name2]), (kw2, [name1, name2, name3])]


