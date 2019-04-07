# coding=utf-8
# author=yphacker

import io
import re
import requests
from zipfile import ZipFile

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
data = requests.get(url).content
zf = ZipFile(io.BytesIO(data))
start_id = ''

# 步骤1
for x in zf.namelist():
    if x.lower().startswith('readme'):
        msg = zf.read(x).decode('utf-8')
        print(msg)
        start_id = re.findall('\\s(\\d+)', msg)[0]
        break

# 步骤2
hints = ''
next_id = start_id
while True:
    fname = next_id + '.txt'
    msg = zf.read(fname).decode('utf-8')
    print(msg)
    info = zf.getinfo(fname)
    # 步骤3
    hints += info.comment.decode('utf-8')
    try:
        next_id = re.findall('\\s(\\d+)', msg)[0]
    except:
        print(hints)
        break
