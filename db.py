import pymongo
from pymongo import Connection
from reflection_scraper import master_list

#$ mongod
connection = Connection()

db = connection.keywords_db
keywords_col = db.keywords_col
keywords_col.insert(master_list)

#for doc in keywords_col.find():
#	print doc

