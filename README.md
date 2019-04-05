# [Python Challenge](http://www.pythonchallenge.com)
所有解题代码，皆可由标题跳转得到
## [Level 0](/code/level_0.py)
![Level 0.gif](/image/level_0.jpg)  
看提示图片中为2**38，计算值为274877906944。  
Hint: try to change the URL address.  
下一关地址：http://www.pythonchallenge.com/pc/def/274877906944.html

## [Level 1](/code/level_1.py)
![Level 1.gif](/image/level_1.jpg)  
Hint 1：K-&gt;M  O-&gt;Q  E-&gt;G  
由Hint 1可知是位移计算，都是位移两位  
Hint 2：g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.  
利用Hint 1的算法转换字符串，得到下一关的地址信息。需要注意的是：转换是在26个字母中转换的  
[代码](/code/level_1.py)  
解密得到：i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.  
根据提示，使用同样的方法转换map，得到ocr  
下一关地址：http://www.pythonchallenge.com/pc/def/ocr.html

## [Level 2](/code/level_2.py)
![Level 2.gif](/image/level_2.jpg)  
根据提示密码也许在图片的书里，也许在网页源代码中。于是查看网页源代码，得到提示：在下面混乱的字符串中找到稀有的字符  
[代码](/code/level_2.py)  
由于稀有字符是有顺序的，所以我使用了有序字典，进行存储字符跟出现次数，得到的结果为：equality  
下一关地址：http://www.pythonchallenge.com/pc/def/equality.html

## [Level 3](/code/level_3.py)  
![Level 3.gif](/image/level_3.jpg)  
Hint: 一个小字母，两边各有三个保镖  
意思就是要找到这么一个小写字母，两边都是三个大写字母，而且两边都要是小写字母，即：xXXXxXXXx  
根据[level2](#level2)可知，也是从网页源代码中找到这些字符  
[代码](/code/level_3.py)  
得到的结果为：linkedlist
访问：http://www.pythonchallenge.com/pc/def/linkedlist.html，得到linkedlist.php
下一关地址：http://www.pythonchallenge.com/pc/def/linkedlist.php

## [Level 4](/code/level_4.py)  
![Level 4.gif](/image/level_4.jpg)  