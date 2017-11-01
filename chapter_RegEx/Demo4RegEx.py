# -*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\9\29 0029 12:38 '
# project = Demo4python
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

m = re.match('foo', 'food on the table')  # 匹配成功
print m.group()

m = re.match('foo', 'seafood')  # 匹配失败
if m is not None: print m.group()

m = re.search('foo', 'seafood')  # 使用search()代替
if m is not None: print m.group()  # 搜索成功，但是匹配失败
print '结束\n匹配多个字符串'

bt = 'bat|bet|bit'  # 正则表达式模式：bat、bet、bit
m = re.match(bt, 'bat')  # ‘bat’ 是一个匹配
if m is not None: print m.group()

print '---------------------'
m = re.match(bt, 'blt')  # 对于 ‘bit’没有匹配
if m is not None: print m.group()
print '---------------------'
m = re.match(bt, 'He bit me!')  # 不能匹配字符串
if m is not None: print m.group()
print '---------------------'
m = re.search(bt, 'He bit me!')  # 通过搜索查找'bit'
if m is not None: print m.group()
print '---------------------\n匹配任何单个字符'

anyend = '.end'
m = re.match(anyend, 'bend')  # 点号匹配‘b’
if m is not None: print m.group()  #

m = re.match(anyend, 'end')  # 不匹配任何字符
if m is not None: print m.group()

m = re.match(anyend, 'end')  # 不匹配任何字符
if m is not None: print m.group()

m = re.match(anyend, '\nend')  # 除了 \n之外的任何字符
if m is not None: print m.group()

m = re.search('.end', 'The end.')  # 在搜索中匹配
if m is not None: print m.group()
print '----------'

patt314 = '3.14'  # 表达正则表达式的点号
pi_patt = '3\.14'  # 表示字面量的点号(dec. point)
m = re.match(pi_patt, '3.14')  # 精确匹配
if m is not None: print m.group()

m = re.match(patt314, '3014')  # 点号匹配‘0’
if m is not None: print m.group()

m = re.match(patt314, '3.14')  # 点号匹配“。”
if m is not None: print m.group()
print '-----创建字符集([ ])---'

m = re.match('[cr][23][dp][o2]', 'c3po')  # 匹配‘c3po’
if m is not None: print m.group()

m = re.match('[cr][23][dp][o2]', 'c2do')  # 匹配‘c3po’
if m is not None: print m.group()

m = re.match('r2d2|c3po', 'c2do')  # 不匹配‘c2do’
if m is not None: print m.group()

m = re.match('r2d2|c3po', 'r2d2')  # 匹配‘r2d2’
if m is not None: print m.group()

'---重复、特殊字符以及分组---'
patt = '\w+@(\w+\.)?\w+\.com'
print re.match(patt, 'nobody@xxx.com').group()

print re.match(patt, 'nobody@xxx.xxx.com').group()
# if re is not None:print re.match(patt,'nobody@xxx.xxx.yyy.com').group()

patt = '\w+@(\w+\.)*\w+\.com'
print re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group()

m = re.match('\w\w\w-\d\d\d', 'abc-123')  # 匹配
if m is not None: print m.group()

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')  # 匹配
if m is not None: print m.group()

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')  # 匹配
# if m is not None:print m.group()
if m is not None: print m.group(1)
if m is not None: print m.group(2)

m = re.match('ab', 'ab')
print m.group()
print m.groups()
print '分组'
m = re.match('(ab)', 'ab')
print m.group()
print m.group(1)
print m.groups()

m = re.match('(a)(b)', 'ab')
print m.group()
print m.group(1)
print m.groups()
print '------'
m = re.match('(a(b))', 'ab')
print m.group()
print m.group(1)
print m.groups()
print '-------'
m = re.search('The', 'The end.')  # 匹配
print m.group()
m = re.search('^The', 'w The end.')  # 不作为起始
if m is not None: print m.group()

m = re.search(r'\bthe', 'bite the dog.')  # 在边界
if m is not None: print m.group()

m = re.search(r'\bthe', 'bitethe dog')  # 有边界
if m is not None: print m.group()

m = re.search(r'\Bthe', 'bitethe dog')  # 没有边界
if m is not None: print m.group()

print '-----findall与finditer-------'
print re.findall('car', 'car')
print re.findall('car', 'scarry')
print re.findall('car', 'scarry the baracardi to the car')

s = 'This and that.'
print re.findall(r'(th\w+) and (th\w+)', s, re.I)

print re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().groups()

print re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().group(1)

print re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().group(2)

print [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)]

print re.findall(r'(th\w+)', s, re.I)

it = re.finditer(r'(th\w+)', s, re.I)
g = it.next()
print g.groups()
print g.group(1)
g = it.next()
print g.groups()
print g.group(1)
print [g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)]

print '---sub()和subn()搜索与替换---'
print 'sub方法--替换'
print re.sub('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')
print 'subn方法--替换(返回替换的个数)'
print re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')

print re.sub('[ae]', 'X', 'abcdef')
print re.subn('[ae]', 'X', 'abcdef')

print '---在限定模式上使用split分隔字符串---'
print re.split(':', 'str1:str2:str3')

DATA = (
    'Mountain View,CA 94040',
    'Sunnuvale,CA',
    'Los Altos 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

for datum in DATA:
    print re.split(', |(?=(?:\d{5}|[A-Z]{2}))', datum)

print '---扩展符号---'
print re.findall(r'(?i)yes', 'yes? Yes. YES!!')

print re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.')
print '---这里 编译器不用加换行符---'
print re.findall(r'(?mi)^th[\w ]+', """This line is the first,\nanther line,\nthat line,it's the best""")
print '---这里 re.S用法展示---'
print re.findall(r'th.+', "The first line \nthe second line \nthe third line")
print re.findall(r'(?s)th.+', "The first line \nthe second line, \nthe third line\n")
print '---这里用x 虽然显示错误，编译却会正常。'
print re.search(r'''(?x)\((\d{3})\)[ ](\d{3})-(\d{4})''', '(800) 555-1212'
                ).groups()

print re.findall(r'http://(?:\w+\.)*(\w+\.com)', "http://google.com "
                                                 "http://www.google.com "
                                                 "http://code.google.com")

print re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212'
                ).groupdict()

print re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(\g<areacode>) (\g<prefix>-xxxx)',
             '(800) 555-1212'
             )

print re.findall(r'\w+(?= van Rossum)', '''Guido van Rossum\nTim Peters\nAlex Martell\nJust van Rossum\nRaymod''')

print re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
                 '''
                 sales@phptr.com
                 postmaster@phptr.com
                 eng@phptr.com
                 noreply@phptr.com
                 admin@phptr.com'''
                 )
print ['%s@aw.com' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
                                               '''
                 sales@phptr.com
                 postmaster@phptr.com
                 eng@phptr.com
                 noreply@phptr.com
                 admin@phptr.com''')]

print bool(re.search(r'(?:(x)|y)(?(1)y|x)','xy'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)','xx'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)','yx'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)','yy'))