import requests

url='https://www.baidu.com/more/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

response=requests.get(url=url,headers=headers)

with open('more.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))