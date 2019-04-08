# coding=utf-8
# author=yphacker

import io
import requests
from PIL import Image

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
png_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
print('loading image, please wait ...')
content = requests.get(png_url).content
img_info = io.BytesIO(content)

img = Image.open(img_info)
w = img.size[0]  # width
h = img.size[1]  # heigh
m = h / 2  # middle

# for i in range(w):
#     p = img.getpixel((i, m))
#     print(chr(p[0]), end="")
# print('\n')

res = []
for i in range(0, w, 7):
    p = img.getpixel((i, m))  # note: m in m-4 ~ m+4 is OK
    if p[0] == p[1] == p[2]:  # also can img.convert("L") first
        res.append(p[0])
img.close()

res = [chr(x) for x in res]
msg = ''.join(res)
print(msg)

start, end = (msg.find('['), msg.find(']'))
nmsg = msg[start + 1:end].split(',')
print(''.join([chr(int(x)) for x in nmsg]))
