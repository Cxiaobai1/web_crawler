# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 22:46
# @Author  : Cxiaobai
# @Email   : 494158341@qq.com
# @File    : 04-微信小程序社区.py
# @Software: PyCharm

import requests

url = 'https://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
params = {
    'mod': 'list',
    'catid': '2',
}
for i in range(1, 11):
    params['page'] = i
    response = requests.get(url=url, headers=headers, params=params)
    with open('第%s页.html' % i, 'w', encoding='utf-8')as fp:
        fp.write(response.text)
        print("第%s页爬取成功" % i)
