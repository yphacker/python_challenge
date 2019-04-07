# coding=utf-8
# author=yphacker

import requests

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
id = '12345'
cnt = 0

while True:
    url = base_url + id
    print(cnt, url)
    content = requests.get(url).content.decode('utf-8')
    if content.find('and the next nothing is') == -1:
        print(content)
        # print data, id
        if content.endswith('.html'):
            break
        elif content.startswith('Yes. Divide by two and keep going.'):
            id = str(int(id) // 2)
    else:
        id = content.split()[-1]

    cnt = cnt + 1
