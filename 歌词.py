import requests,json
from bs4 import BeautifulSoup
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头
usl1='https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html'

music=requests.get(usl1,headers=headers)
musid1=BeautifulSoup(music.text,'html.parser')
text=musid1.find_all('div',class_="mod_lyric")
for text1 in text:
    music_text=text1.find('div',class_='lyric__cont_box').find('p').text
    print(music_text)

