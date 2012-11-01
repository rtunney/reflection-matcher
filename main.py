import request 
import reflection_scraper 
import db


request.download_reflections_pages()
master_list = reflection_scraper.get_peoples_words()
print master_list
db.save_words_in_reflections(master_list)
