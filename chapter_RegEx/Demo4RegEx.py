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

m = re.match('foo','food on the table') #匹配成功
print m.group()

m = re.match('foo','seafood') # 匹配失败
if m is not None:print m.group()

m = re.search('foo','seafood') # 使用search()代替
if m is not None:print m.group() # 搜索成功，但是匹配失败
print '结束\n匹配多个字符串'

bt = 'bat|bet|bit' # 正则表达式模式：bat、bet、bit
m = re.match(bt,'bat')  # ‘bat’ 是一个匹配
if m is not None: print m.group()

print '---------------------'
m = re.match(bt,'blt') # 对于 ‘bit’没有匹配
if m is not None:print m.group()
print '---------------------'
m = re.match(bt,'He bit me!') # 不能匹配字符串
if m is not None: print m.group()
print '---------------------'
m = re.search(bt,'He bit me!') # 通过搜索查找'bit'
if m is not None:print m.group()
print '---------------------\n匹配任何单个字符'

anyend = '.end'
m = re.match(anyend,'bend') # 点号匹配‘b’
if m is not None: print m.group() #

m = re.match(anyend,'end') # 不匹配任何字符
if m is not None:print m.group()

m = re.match(anyend,'end') # 不匹配任何字符
if m is not None: print m.group()

m = re.match(anyend,'\nend') # 除了 \n之外的任何字符
if m is not None: print m.group()

m = re.search('.end','The end.') # 在搜索中匹配
if m is not None:print m.group()
print '----------'

patt314 = '3.14'   # 表达正则表达式的点号
pi_patt = '3\.14'  # 表示字面量的点号(dec. point)
m = re.match(pi_patt, '3.14') # 精确匹配
if m is not None:print m.group()

m = re.match(patt314,'3014') # 点号匹配‘0’
if m is not None:print m.group()

m = re.match(patt314,'3.14') # 点号匹配“。”
if m is not None:print m.group()
print '-----创建字符集([ ])---'

m = re.match('[cr][23][dp][o2]','c3po') # 匹配‘c3po’
if m is not None:print m.group()

m = re.match('[cr][23][dp][o2]','c2do') # 匹配‘c3po’
if m is not None:print m.group()

m = re.match('r2d2|c3po','c2do') # 不匹配‘c2do’
if m is not None:print m.group()

m = re.match('r2d2|c3po','r2d2') # 匹配‘r2d2’
if m is not None:print m.group()

'---重复、特殊字符以及分组---'
patt = '\w+@(\w+\.)?\w+\.com'
print re.match(patt,'nobody@xxx.com').group()


print re.match(patt,'nobody@xxx.xxx.com').group()
#if re is not None:print re.match(patt,'nobody@xxx.xxx.yyy.com').group()

patt = '\w+@(\w+\.)*\w+\.com'
print re.match(patt,'nobody@www.xxx.yyy.zzz.com').group()

m = re.match('\w\w\w-\d\d\d','abc-123') # 匹配
if m is not None:print m.group()

m = re.match('\w\w\w-\d\d\d','abc-xyz') # 匹配
if m is not None:print m.group()

m = re.match('(\w\w\w)-(\d\d\d)','abc-123') # 匹配
#if m is not None:print m.group()
if m is not None:print m.group(1)
if m is not None:print m.group(2)