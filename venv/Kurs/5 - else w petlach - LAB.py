import os
import urllib.request
from urllib.request import URLError
#os.rmdir(r"c:\\temp")
#os.mkdir(r'c:\\temp\\')
datadir = r'c:\\temp\\'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'abc', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'},
    { 'name': 'onet',       'url': 'https://onet.pl'} ]

html = '.html'
#path = datadir + pages
for page in pages:
    try:
        respose = urllib.request.urlopen(page['url'])
        print(f"Connected to {page['url']}")
        path = datadir  + page['name'] + html
        print(path)
        urllib.request.urlretrieve(page['url'], path) #pobieranie strony

    except URLError as e:
         print(f"Failed to connect to {page['url']}: {e}")

else:
    print('All done.')


