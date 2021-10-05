import re
import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['阅读数', '评论数', '标题', '作者', '时间'])

url = 'https://guba.eastmoney.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

response = requests.get(url=url, headers=headers)
# print(response.text)

ul_patter = re.compile('<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>', re.S)
ul_res = ul_patter.findall(response.text)[0]
# print(ul_res)
li_patter = re.compile('<li.*?>(.*?)</li>', re.S)
li_res = li_patter.findall(ul_res)
# print(li_res)
cite_patter = re.compile('<cite>(.*?)</cite>', re.S)
title_patter = re.compile('<span.*? title="(.*?)" class="note">.*?</span>', re.S)
aut_patter = re.compile('<cite class="aut">.*?<font>(.*?)</font>.*?</cite>', re.S)
time_patter = re.compile('<cite class="last">(.*?)</cite>', re.S)
for i in range(0, len(li_res)):
    cite_res_read = cite_patter.findall(li_res[i])[0].strip()
    cite_res_comment = cite_patter.findall(li_res[i])[1].strip()
    res_title = title_patter.findall(li_res[i])[0]
    res_aut = aut_patter.findall(li_res[i])[0]
    res_time = time_patter.findall(li_res[i])[0]
    ws.append([cite_res_read, cite_res_comment, res_title, res_aut, res_time])
wb.save('股吧.xlsx')
print('爬取成功')
