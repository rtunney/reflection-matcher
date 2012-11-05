from bs4 import BeautifulSoup
import os
import re

#create_frequency_dict can't handle keywords with characters like
#+, *, or ? that have special meanings in regex

def get_keywords(filename):
  keywords = []
  f = open(filename, 'r')
  for line in f:
    keywords.append(line.strip())
  return keywords

def create_frequency_dict(keywords, reflection_str):
  frequency_dict = {}
  for keyword in keywords:
    re_keyword = re.compile('(?:\A|\W)' + re.escape(keyword) + '(?:\W|\Z)', re.IGNORECASE)
    count = len(re_keyword.findall(reflection_str))
    if count > 0:
      frequency_dict[keyword] = count
  return frequency_dict

def create_db_entry (keywords, name, reflection_str):
  db_entry = {}
  db_entry['name'] = name
  frequency_dict = create_frequency_dict(keywords, reflection_str)
  db_entry['keywords'] = frequency_dict
  return db_entry

def create_master_list(keywords, reflections_dict):
  master_list = []
  for name, reflection_str in reflections_dict.iteritems():
    db_entry = create_db_entry(keywords, name, reflection_str)
    master_list.append(db_entry)
  return master_list

def get_file_names(dir_path):
  files = os.listdir(dir_path)
  for index, file_name in enumerate(files):
    files[index] = dir_path + file_name
  return files

def get_reflections(file_names):
  reflections = []
  for file in file_names:
    doc = BeautifulSoup(open(file))
    reflections += doc.select('.reflections-for-day > li')
  return reflections

def scrape_reflections(reflections):
  reflections_dict = {}
  for reflection in reflections:
    name = reflection.a.string[:-1]
    for p in reflection('p'):
      reflections_dict[name] = reflections_dict.get(name, "") + str(p.string).lstrip().lower()
  return reflections_dict

KEYWORDS_FILENAME = "keywords.txt"
def get_master_list():
  keywords = get_keywords(KEYWORDS_FILENAME)
  file_names = get_file_names('html/')
  reflections = get_reflections(file_names)
  reflections_dict = scrape_reflections(reflections)
  master_list = create_master_list(keywords, reflections_dict)
  return master_list
