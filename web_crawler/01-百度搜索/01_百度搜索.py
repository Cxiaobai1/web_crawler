import requests

url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
wd=input("请输入要搜索的内容：")
params = {
    "wd": wd,
    "rsv_spt": "1",
    "rsv_iqid": "0xef54f3de00169da4",
    "issp": "1",
    "f": "8",
    "rsv_bp": "1",
    "rsv_idx": "2",
    "ie": "utf - 8",
    "tn": "baiduhome_pg",
    "rsv_dl": "tb",
    "rsv_enter": "1",
    "rsv_sug3": "7",
    "rsv_sug1": "1",
    "rsv_sug7": "100",
    "rsv_sug2": "0",
    "rsv_btype": "i",
    "inputT": "895",
    "rsv_sug4": "1562",
}
response = requests.get(
    url=url,
    headers=headers,
    params=params,
)
# print(response.request.headers)
# print(response.url)

with open(wd+'.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
