import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url)
print("Retrieving: ",url)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info["comments"]))

sum = 0
for item in info["comments"]:
    # print('Name', item['name'])
    # print('Count', item['count'])

    sum += item['count']

print('Sum:',sum)