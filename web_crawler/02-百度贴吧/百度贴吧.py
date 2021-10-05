import requests

url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

params = {
    'kw': 'lol',
    'ie': 'utf-8',
}
for i in range(1, 6):
    params['pn'] = 50 * (i - 1)
    response = requests.get(headers=headers, url=url, params=params)
    with open('第%d页'%i + '.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)

# print(response.text)
