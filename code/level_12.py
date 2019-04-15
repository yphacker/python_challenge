# coding=utf-8
# author=yphacker

import os
from PIL import Image, ImageFile
import requests
from requests.auth import HTTPBasicAuth

'''python challenge level 12
question url: http://www.pythonchallenge.com/pc/return/evil.html
answer url: http://www.pythonchallenge.com/pcc/return/.html
'''

ImageFile.LOAD_TRUNCATED_IMAGES = True

username = 'huge'
password = 'file'

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
gfx = requests.get(url, auth=HTTPBasicAuth(username, password)).content
img = Image.new('RGB', (3200, 480))
for i in range(5):
    filename = '{}.jpg'.format(i)
    file = open(filename, 'wb')
    file.write(gfx[i::5])
    im = Image.open(filename)
    print(im.size)
    img.paste(im, (i * 640, 0))
    if os.path.exists(filename):
        os.remove(filename)

img.show()
