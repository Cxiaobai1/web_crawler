# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 22:57
# @Author  : Cxiaobai
# @Email   : 494158341@qq.com
# @File    : 05-正则表达式.py
# @Software: PyCharm

import re

# 例字符串
str = '1hello2world'

# compile制订规则
patter = re.compile(r'\d')

# match()匹配 从左往右匹配一次返回match对象，若不符合匹配，返回none
res_match = patter.match(str)
print(res_match.group())

# search()匹配 全局匹配，只匹配成功一次返回match对象，若不符合匹配，返回none
res_search = patter.search(str)
print(res_search.group())

# findall()匹配 全局匹配 ，返回所有符合条件的列表,若没有符合，返回空列表
res_findall = patter.findall(str)
print(res_findall)

# finditer()匹配 全局匹配,返回可迭代对象 callable_iterator
res_finditer = patter.finditer(str)
for i in res_finditer:  # match对象
    print(i.group())

html='<div>python</div><div>java</div><div>c</div><div>PHP</div>'
patter=re.compile(r'<div>(.*?)</div>')
res=patter.findall(html)
print(res)