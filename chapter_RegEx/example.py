#-*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\11\2 0002 11:14 '
project = 'Demo4python'
"""
description=example 
"""
'''
import os
import re

f = os.popen('tasklist /nh','r')
for eachline in f:
    print re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',eachline.rstrip())

f.close()
'''

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime
import re
'''
tlds = ('com','edu','net','org','gov')

for i in xrange(randrange(5, 11)):
    dtint = randrange(maxint)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in xrange(llen))
    dlen = randrange(llen,13) #domain is longer
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr,login,dom,choice(tlds),dtint,llen,dlen)
    log = '%s::%s@%s.%s::%d-%d-%d' % (dtstr,login,dom,choice(tlds),dtint,llen,dlen)

patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt,log)
print m.group()
print m.group(1)
print m.groups()

patt = '^(\w{3})'
m = re.match(patt,log)
print m.group()
print m.group(1)
print m.groups()
'''
print '匹配后续的字符串：“bat”、“bit”'
patt = '(b[aeicu]t)'
m = re.search(patt,r'webat,but')
if m is not None: print m.groups()

print '匹配后续的单词对”'
patt = '\w+ \w+'
m = re.match(patt,r'Veyron Romeo')
if m is not None: print m.group()

print '匹配首字符'
patt = '^(\w{1})'
m = re.match(patt,r'Vey ron')
if m is not None: print m.group()
'''
print '匹配标识符'
m = re.findall('','',re.L)
if m is not None: print m.groups()
'''
print '匹配街道'
patt = r'^(\d+ \w+ \w* \w* \w*)'
m = re.match(patt,'3120 De la Cruz Boulevard',re.L)
if m is not None: print m.group()

print '匹配网址'
patt = r'^www.*\.com$'
m = re.match(patt,'www.dsa5d.com.com')
if m is not None: print m.group()

m = type(0)
print m