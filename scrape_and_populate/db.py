from pymongo import Connection

connection = Connection()

def populate_reflections_db(master_list):
	db = connection.reflections
	collection = db.words
	collection.remove()
	collection.insert(master_list)

#for doc in db.words.find({"keywords.json" : {$exists : true}}):
#	print doc

#print collection.find_one({'keywords':})
#for doc in keywords_col.find():
#	print doc
