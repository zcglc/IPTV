import gevent
#导入gevent、time、requests。
import json,bs4,zipfile,time,requests
from bs4 import BeautifulSoup
from gevent.queue import Queue
from gevent import monkey
#从gevent库里导入monkey模块。
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

start=time.time()
url_list=[]
url_list2=[]
url_list3=[]

def url_ture():
    for i in range(11):
        url1='http://www.font5.com/Font_Classification/Font_Classification_%s_1.html' % (i+1)
        url_list.append(url1)
    url2='http://www.font5.com/Font_Classification/Font_Classification_38_1.html'
    url_list.append(url2)

def url_ture2():
    url='http://www.font5.com/Font_Classification/Font_Classification_1_1.html'
    A=requests.get(url,headers=headers)
    B=BeautifulSoup(A.text,'html.parser')
    C=B.find_all('div',class_="cleft_list")[1].find_all('li')
    for i in C:
        url_small=i.find('a')['href']
        url_list.append('http://www.font5.com/'+url_small)

def url2():
    try:
        for a in url_list:
            page=requests.get(a,headers=headers)
            page.encoding='gbk'
            page1=BeautifulSoup(page.text,'html.parser')
            page2=page1.find('div',class_="cr_pages").find_all('option')
            for page3 in page2:
                page_url=page3['value']
                #num_name=page3.text
                url_list2.append('http://www.font5.com'+page_url)
    except AttributeError:
        pass
    for url in url_list2:
        url11=requests.get(url,headers=headers)
        url11.encoding='gbk'
        font1=BeautifulSoup(url11.text,'html.parser')
        font_zero=font1.find_all('div',class_="vt2l")
        for i in font_zero:
            fo=i.find('a')['href']
            url_list3.append('http://www.font5.com'+fo)
    
url_ture()
url_ture2()            
url2()

work=Queue()

for url in url_list3:
    work.put_nowait(url)

def crawler():
    while not work.empty():
        try:
            url=work.get_nowait()
            font=requests.get(url,headers=headers)
            font.encoding='gbk'
            one=BeautifulSoup(font.text,'html.parser')
            font_o=one.find('div',class_="info_right").find_all('tr')[7]
            font_get=font_o.find(class_='tab2').find('a')['href']
            get='http://www.font5.com'+font_get

            getin=requests.get(get,headers=headers)
            getin.encoding='gbk'
            a=BeautifulSoup(getin.text,'html.parser')
            font_one=a.find('div',class_="m1_text").find('a')['href']
            font_name=a.find('div',class_="vt2l").find('span').text[:-5]

            b=requests.get(font_one,headers=headers)
            b.encoding='gbk'
            bb=b.content 
                        
            ziti='F:\\字体\\'+font_name+'.zip'
            with open(ziti,'wb')as ff:
                ff.write(bb)
                ff.close

            zip_file = zipfile.ZipFile(ziti)
            zip_list = zip_file.namelist() # 得到压缩包里所有文件

            for f in zip_list:
                zip_file.extract(f, 'F:\\字体\\解压') # 循环解压文件到指定目录
            zip_file.close() # 关闭文件，必须有，释放内存
        except NotImplementedError:
            pass            
tasks_list=[]

for x in range(20):
    task=gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)

print('爬取结束')
end=time.time()
print('用时：'+str(end-start))