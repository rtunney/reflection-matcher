==========
PairWise
==========

PairWise is an app designed to match Hacker Schoolers on the basis of 
common keywords used in their reflections. 

Data Scraping and Storage
---------------------------

main.py is executed to scrape up-to-date reflections data. 

main.py uses request.py, reflection_scraper.py, and db.py

* request.py opens a session on hackerschool.com, requests the source
code for reflections pages, and writes these files to the html folder.

* reflection_scraper.py uses python's beautiful soup 4 module to parse
the html of the pages and create a db_entries list of entries in the 
form {'name':<HSer full name>, 'keywords':{'kw1':freq, 'kw2':freq ...}}
with freq=numInstances of kw in HSer's reflections data.

* db.py opens a connection to a mongoDB and dumps db_entries in the db 

Server
---------

PairWise is built with Flask (server.py listens on localhost:5000).

index.html is served and its form expects the full name of the HSer 
as listed on the reflections page (e.g."Robert Tunney").

Upon submission, generate_tree is called in tree.js. In generate_tree, 
d3.json sends a get request to '/<HSer full name>'. The server queries
mongo and packages a json object with name/keywords/match_names that is
expected by the d3 tree template. Generate_tree renders the tree and sticks
it in the page. 

Misc.
----------
To run request.py or main.py, you need to set REFLECTION_ID to your
HS login and REFLECTION_SECRET to your HS password in your environmental
variables. 

Ignore
----------
Procfile & requirements.txt 

To Do: 
----------
* Implement smart identification of keywords from reflections text
* Add functionality to tree display (access individuals' reflections
text, collapse branches of tree)
