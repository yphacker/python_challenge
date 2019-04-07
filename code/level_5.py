# coding=utf-8
# author=yphacker

import pickle
import requests

url = "http://www.pythonchallenge.com/pc/def/banner.p"
content = requests.get(url).content
data = pickle.loads(content)
print(data)

info = ''
for item in data:
    for x in item:
        info += x[0] * int(x[1])
    info += '\n'

print(info)
