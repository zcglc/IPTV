import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
def picturedonman():

    
    url='http://pic.netbian.com/4kdongman/index.html'
    picture=requests.get(url,headers=headers,timeout=None)
    picture.encoding='gbk'
    picture_all=BeautifulSoup(picture.text,'html.parser')    
    picture_one=picture_all.find('ul',class_="clearfix").find_all('li')
    
    for name in picture_one:
        nameone=name.find('a')['href']
        nametwo=name.find('img')['src']
        namethree=name.find('b').text
        
        print('图片A系列')
        print('%s+%s+%s' % (nameone,nametwo,namethree))
        print('------------------------------------')
        #读取每一个图片
        http='http://pic.netbian.com'+nameone
        zero=requests.get(http,headers=headers,timeout = None)
        zeroone=BeautifulSoup(zero.text,'html.parser')
        zerotwo=zeroone.find('a',id='img')
        img=zerotwo.find('img')
        img_true=img['src']
        #进入新链接
        wendan_name='图片A系列'
        wendan_nameone=namethree
        truename='d:\\素材\\dssd\\3131\\'+wendan_name+wendan_nameone+'.jpg'
        truepictrue='http://pic.netbian.com'+img_true
        truepictruenow=requests.get(truepictrue,headers=headers,timeout=None)
        one=truepictruenow.content
        with open(truename,'wb') as tupian:
            tupian.write(one)
            tupian.close()
        #储存图片

    

def picturedonman1():
        
    for i in range(142):
        url='http://pic.netbian.com/4kdongman/index_%s.html' % (i+2)
        picture=requests.get(url,headers=headers,timeout=None)
        picture.encoding='gbk'
        picture_all=BeautifulSoup(picture.text,'html.parser')    
        picture_one=picture_all.find('ul',class_="clearfix").find_all('li')
        
        for name in picture_one:
            nameone=name.find('a')
            nametwo=name.find('img')
            namethree=name.find('b')
            nameone1=nameone['href']
            nametwo1=nametwo['src']
            namethree1=namethree.text
        #读取每一个图片
            http='http://pic.netbian.com'+nameone1
            zero=requests.get(http,headers=headers,timeout=None)
            zeroone=BeautifulSoup(zero.text,'html.parser')
            zerotwo=zeroone.find('a',id='img')
            img=zerotwo.find('img')
            img_true=img['src']
        #进入新链接

            wendan_name='图片A系列 '
            wendan_nameone=namethree1
            truename='d:\\素材\\dssd\\3131\\'+wendan_name+wendan_nameone+'.jpg'
            truepictrue='http://pic.netbian.com'+img_true
            truepictruenow=requests.get(truepictrue,headers=headers,timeout=None)
            one=truepictruenow.content
            with open(truename,'wb') as tupian:
                tupian.write(one)
                tupian.close()
            #储存图片    

            print('图片A系列 ')
            print('%s+%s+%s' % (nameone1,nametwo1,namethree1))
            print('------------------------------------')
picturedonman()
picturedonman1()
