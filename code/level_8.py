# coding=utf-8
# author=yphacker

import re
import bz2
import requests

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
content = requests.get(url).content#.decode('utf-8')
un = re.findall(b"un: '([^']+)'", content)[0]
pw = re.findall(b"pw: '([^']+)'", content)[0]
print(un)
print(pw)

print('username:', bz2.decompress(un.decode('unicode_escape').encode('latin1')))
print('password:', bz2.decompress(pw.decode('unicode_escape').encode('latin1')))
