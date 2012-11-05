import request 
import reflection_scraper 
import db

request.main()
master_list = reflection_scraper.get_master_list()
db.populate_reflections_db(master_list)