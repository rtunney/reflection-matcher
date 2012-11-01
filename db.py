from pymongo import Connection

connection = Connection()

def save_words_in_reflections(word_list):
	db = connection.reflections
	collection = db.words
	collection.remove({})
	collection.insert(word_list)

#for doc in db.words.find({"keywords.json" : {$exists : true}}):
#	print doc

#print collection.find_one({'keywords':})
#for doc in keywords_col.find():
#	print doc
