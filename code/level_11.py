# coding=utf-8
# author=yphacker

import io
from PIL import Image
import requests
from requests.auth import HTTPBasicAuth

username = 'huge'
password = 'file'

img_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
content = requests.get(img_url, auth=HTTPBasicAuth(username, password)).content
img_info = io.BytesIO(content)
img = Image.open(img_info)
# img.show()

srcimg = img
new_img = Image.new(img.mode, srcimg.size)
for w in range(0, img.size[0], 2):
    for h in range(0, srcimg.size[1], 2):
        new_img.putpixel((w, h), srcimg.getpixel((w, h)))
new_img.show()
