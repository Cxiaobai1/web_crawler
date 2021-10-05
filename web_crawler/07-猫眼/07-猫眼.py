import requests
import re
from openpyxl import Workbook

with open(r'C:\Users\49415\PycharmProjects\pythonProject\爬虫\07-猫眼\maoyan.html', 'r', encoding='utf-8') as fp:
    response = fp.read()
    # print(fp.read())

wb = Workbook()
ws = wb.active
ws.append(['排名', '片名', '主演', '上映时间', '评分'])
dl_patter = re.compile('<dl class="board-wrapper">(.*?)</dl>', re.S)
dl_res = dl_patter.findall(response)[0]
# print(len(dl_res))
dd_patter = re.compile('<dd>(.*?)</dd>', re.S)
dd_res = dd_patter.findall(dl_res)
# print(dd_res)
i_patter = re.compile('<i class="board-index board-index-.*?">(.*?)</i>', re.S)
div_patter = re.compile('<p class="name"><a.*? title="(.*?)".*?</a></p>', re.S)
star_patter = re.compile('<p class="star">.*?主演：.*?(.*?)</p>', re.S)
time_patter = re.compile('<p class="releasetime">(.*?)</p>', re.S)
score_integer_patter = re.compile('<p class="score"><i class="integer">(.*?)</i>.*?</p>', re.S)
score_fraction_patter = re.compile('<p class="score">.*?<i class="fraction">(.*?)</i></p>', re.S)
for i in range(0, len(dd_res)):
    i_res = i_patter.findall(dd_res[i])[0]
    title_res = div_patter.findall(dd_res[i])[0]
    star_res = star_patter.findall(dd_res[i])[0].strip()
    time_res = time_patter.findall(dd_res[i])[0]
    score_integer_res = score_integer_patter.findall(dd_res[i])[0]
    score_fraction_res = score_fraction_patter.findall(dd_res[i])[0]
    score_res = score_integer_res + score_fraction_res
    ws.append([i_res, title_res, star_res, time_res, score_res])
    # print(i_res, title_res, star_res, time_res, score_res)
wb.save('猫眼.xlsx')
print("爬取成功")