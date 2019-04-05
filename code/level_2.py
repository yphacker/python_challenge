# coding=utf-8
# author=yphacker

import re
import requests
import collections

url = r'http://www.pythonchallenge.com/pc/def/ocr.html'
content = requests.get(url).content.decode('utf-8')
m = re.findall('<!--([^>]+)-->', content)


def count_str(s):
    char_list = []
    char_num = []
    for char in s:
        if char in char_list:
            continue
        char_list.append(char)
    for char in char_list:
        char_num.append(s.count(char))
    return collections.OrderedDict(zip(char_list, char_num))


dic = count_str(m[1])
ans = []
for k, v in dic.items():
    # print(k, v)
    if v == 1:
        ans.append(k)
print(''.join(ans))
