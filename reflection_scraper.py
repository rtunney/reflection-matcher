from bs4 import BeautifulSoup
import os
import re

def get_keywords(filename):
  keywords = []
  f = open(filename, 'r')
  for line in f:
    keywords.append(line.strip())
  return keywords

def create_frequency_dict(keywords, reflection_str):
  frequency_dict = {}
  for keyword in keywords:
    keyword = re.compile('(?:\A|\W)' + keyword + '(?:\W|\Z)', re.IGNORECASE)
    count = len(keyword.findall(reflection_str))
    if count > 0:
      frequency_dict[keyword] = count
  return frequency_dict

def create_master_dict(keywords, reflections_dict):
  master_dict = {}
  for name, reflection_str in reflections_dict.iteritems():
    frequency_dict = create_frequency_dict(keywords, reflection_str)
    master_dict[name] = frequency_dict
  return master_dict

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

keywords = get_keywords(KEYWORDS_FILENAME)
file_names = get_file_names('html/')
reflections = get_reflections(file_names)
reflections_dict = scrape_reflections(reflections)
master_dict = create_master_dict(keywords, reflections_dict)

print master_dict
