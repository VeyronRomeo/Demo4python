#-*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\9\29 0029 12:38 '
#project = Demo4python
"""
description=
"""
# coding=utf-8

import re

"""
1.complie(pattern,flags = 0)
没有预编译
2.match(pattern,string,flags=0)
3.search(pattern,string,flags=0)
4.findall(pattern,string,[,flags])
5.finditer(pattern,string,[,flags])
6.split(pattern,string,max=0)

7.sub(pattern,repl,string,count=0)
8.purge()
9.group(num = 0)
10.groupdict(default=None)

11.re.I
12.re.S
"""

m = re.match('foo', 'foo')
if m is not None:
    print m.group()
