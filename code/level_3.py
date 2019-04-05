# coding=utf-8
# author=yphacker

import re
import requests
import collections

url = r'http://www.pythonchallenge.com/pc/def/equality.html'
content = requests.get(url).content.decode('utf-8')
print(''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content)))
