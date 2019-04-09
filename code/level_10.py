# coding=utf-8
# author=yphacker

import re


def describe(s):
    lists = [str(len(m.group(0))) + m.group(1) for m in re.finditer(r"(\d)\1*", s)]
    # print lists
    return "".join(lists)


s = "1"
for i in range(30):
    s = describe(s)
    print(s)
print(len(s))
