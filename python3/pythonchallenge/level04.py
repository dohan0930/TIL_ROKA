import requests
import re

charref = re.compile('[\d]+')
URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'

response = requests.get(URL)
html = response.text
url_num = charref.findall(html)
print(url_num)

while(1):
	URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + url_num[0]
	response = requests.get(URL)
	html = response.text
	url_num = charref.findall(html)
	print(url_num)
