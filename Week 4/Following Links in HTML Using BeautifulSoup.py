# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
pos = int(input("Enter the position"))
count = int(input('Enter the no of counts.'))

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count-1):
    link = tags[pos-1].get('href', None)
    print('Retrieving: ',link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

link = tags[pos-1].get('href', None)
print("Required Url: ",link)
link = tags[pos-1].contents[0]
print("Required User: ",link)

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
