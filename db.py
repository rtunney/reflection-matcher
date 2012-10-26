from pymongo import Connection
from reflection_scraper import master_list

connection = Connection()

db = connection.reflections
collection = db.words
collection.insert(master_list)

#for doc in db.words.find({"keywords.json" : {$exists : true}}):
#	print doc

#print collection.find_one({'keywords':})
#for doc in keywords_col.find():
#	print doc

