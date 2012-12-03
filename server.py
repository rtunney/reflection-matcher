from flask import Flask, render_template, request, send_from_directory
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

#How do we return an icon???
@app.route('/favicon.ico')
def get_icon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'pw.ico')

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

	kw_matches_by_name = {}

	for keyword in my_keywords:
		word_data = {}
		word_data['name'] = keyword
		word_data['children'] = []

		match_names = []
		match_docs = collection.find({'keywords.'+keyword:{'$exists':True}}).sort('keywords.'+keyword, -1)
		
		#INCLUDE TO LIMIT MATCHES BY WORD
		#for match_doc in match_docs[:10]:
		for match_doc in match_docs[:10]:
			match_name = match_doc['name']
			if match_name != name:
				match_names.append(match_name)
				kw_matches_by_name[match_name] = kw_matches_by_name.get(match_name, 0) + 1

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

	match_data['top'] = max(kw_matches_by_name, key=kw_matches_by_name.get)

	return json.dumps(match_data)
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


