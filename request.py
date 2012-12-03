# This Python file uses the following encoding: utf-8
# the line above allows me to use a checkmark
# s.get requests bypass https with verify=False argument
# can you merge multiple html files into one file???

import re
import os
import requests

def get_session(email, password, host='https://www.hackerschool.com'):
    s = requests.session()
    #host = 'http://localhost:5000'
    # This request is to get the CSRF token (the point of which is to make sure other websites
    #  can't make requests on your behalf I think, something to with cross-site scripting
    #  http://en.wikipedia.org/wiki/Cross-site_request_forgery
    r = s.get(host+'/login', verify=False)
    m = re.search(r'<meta content="([a-zA-Z0-9/=+]+)" name="csrf-token"', r.content)
    # This exactly mimics the POST requst that happens when you log in
    payload = {
        'authenticity_token' : m.group(1),
        'email': email,
        'password' : password,
        'commit':'Log In',
        'utf8' : u'✓',
        }
    r = s.post(host+'/sessions', data=payload, verify=False)
    return s

def download_reflections_pages():
    '''downloads all reflection pages and stores them in a folder called html'''
    host = 'https://hackerschool.com'
    email = os.environ.get('REFLECTION_ID')
    password = os.environ.get('REFLECTION_SECRET')
    s = get_session(email, password) 

    if not os.path.exists ("html"):
        os.mkdir ("html")
    r = s.get(host+'/reflections?page=0', verify=False)
    last_page = int(re.search(r'class="last">\s+<a href="/reflections[?]page=(\d+)">', r.text).group(1))

    for pageIndex in range(1, last_page + 1):
      r = s.get(host+'/reflections?page={0}'.format (pageIndex), verify=False)
      f = open("html/reflections_page_{0}.html".format(pageIndex), "w")
      f.write(r.text.encode('utf8'))
      f.close()
if __name__ == '__main__':
    download_reflections_pages()