import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url='http://pic.netbian.com/4kdongman/'

def aderss():
    one=requests.get(url,allow_redirects = False,headers=headers)
    picture_adress=BeautifulSoup(one.text,'html.parser')
    beasons=picture_adress.find('class_="clearfix"')
    for beason in beasons:
        beason_one=beason.find_all('li').find('a')    
        print(beason_one)
aderss()