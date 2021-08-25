import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the ancchor tags
tags = soup('a')
print(tags)
print("_________")
for tag in tags:
    print(tag.get('href', None))