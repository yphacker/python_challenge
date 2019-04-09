# coding=utf-8
# author=yphacker

import re
import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
from PIL import ImageDraw

username = 'huge'
password = 'file'

url = 'http://www.pythonchallenge.com/pc/return/good.html'
data = requests.get(url, auth=HTTPBasicAuth(username, password)).content.decode('utf-8')
comment = re.findall('<!--([^-]+)-->', data)[1]
first = re.findall('first:\n([\d,\n]+)\n', comment)[0].replace('\n', '').split(',')
second = re.findall('second:\n([\d,\n]+)\n', comment)[0].replace('\n', '').split(',')
first = [int(x) for x in first]
second = [int(x) for x in second]
# print(first)
# print(second)

im = Image.new('RGB', (800, 800), )
draw = ImageDraw.Draw(im)
draw.line(first)
draw.line(second)
im.show()
