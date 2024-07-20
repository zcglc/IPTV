
import imp


def a():
    import gevent
    #导入gevent、time、requests。
    #monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
    from gevent import monkey
    #从gevent库里导入monkey模块。
    monkey.patch_all()
    import json,bs4,zipfile,time,requests,sys
    from requests.packages import urllib3
    urllib3.disable_warnings()
    from bs4 import BeautifulSoup
    from gevent.queue import Queue

    print('主人，收集姬开始工作啦！！(づ◡ど)')

    start=time.time()
    work = Queue()

    url_small=[]
    col_listall = []

    def one():
        Apicture=requests.get('https://anime-pictures.net/',verify=False)
        time.sleep(1)
        Apicture.close()
        Bpicture=BeautifulSoup(Apicture.text,'html.parser')
        Cpicture=Bpicture.find('div',class_="post_content index_page")
        Dpicture=Bpicture.find_all('div',class_="post_content index_page")[1]
        Epicture=Bpicture.find_all('div',class_="post_content index_page")[2]
        Fpicture=Bpicture.find('div',class_='last_scores_body').find_all('a')
        for i in Fpicture:
            dpic=i['href']
            url_small.append('https://anime-pictures.net'+dpic)
        for all in Cpicture:
            try:
                pa1=all.find('a')['href']
                url_small.append('https://anime-pictures.net'+pa1)
            except TypeError:
                pass
        for all in Dpicture:
            try:
                pa2=all.find('a')['href']
                url_small.append('https://anime-pictures.net'+pa2)
            except TypeError:
                pass
        for all in Epicture:
            try:
                pa3=all.find('a')['href']
                url_small.append('https://anime-pictures.net'+pa3)
            except TypeError:
                pass
    one()    

    for url in url_small:
    #遍历url_list
        work.put_nowait(url)
        #用put_nowait()函数可以把网址都放进队列里。

    def crawler():
        while not work.empty():
        #当队列不是空的时候，就执行下面的程序。
            try:
                url = work.get_nowait()
                down_dizhi=requests.get(url,verify=False)
                time.sleep(1)
                down_dizhi.close()
                down=BeautifulSoup(down_dizhi.text,'html.parser')
                p_leixin=down.find('picture').find('img')['src'][-4:]
                down_f=down.find(id="rating")
                num=down_f.find_all('a')[1]
                down_ture=num['href']
                name11=down.find(class_="post_content")
                c=name11.find('h1').text
                f=c.split()
                d=''.join(f)
                name1=d[4:]

                with open('E:\\日常getyou\\cookies.txt',
                        'r') as f:
                    for line in f:
                        col_listall.append(line.strip('\n'))
                    f.close()

                if name1 not in col_listall:
                    url2='https://anime-pictures.net'+down_ture
                    tu=requests.get(url2)
                    time.sleep(1)
                    tu.close()
                    tu2=tu.content

                    #time1 = datetime.datetime.now()
                    #time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S') 
                    #name2=name1+time1_str
                    #name=name2.replace(':','_')

                    pname='E:\\日常getyou\\'+'it’s name is '+name1+p_leixin
                    photo = open(pname,'wb')
                    # 写入图片的二进制内容
                    photo.write(tu2) 
                    # 关闭文件
                    photo.close()
                    print('新新的东西+1')
                    with open('E:\\日常getyou\\cookies.txt','a')as coo:
                        coo.write(name1+'\n')
                        coo.close()
                else :
                    print('这次没有收获呢')
                    pass
            except AttributeError:
                print('o(*≧д≦)o!! 出错了，哇啊')
                pass
            except ConnectionError:
                print('o(*≧д≦)o!! 出错了，哇啊')
                pass
    tasks_list  = [ ]
    #创建空的任务列表
    for x in range(2):
    #相当于创建了2个爬虫
        task = gevent.spawn(crawler)
        #用gevent.spawn()函数创建执行crawler()函数的任务。
        tasks_list.append(task)
        #往任务列表添加任务。
    gevent.joinall(tasks_list)

    end=time.time()
    print('此次工作结束\n成功后读取时间：'+str(end-start)+'\n')
def go_time():
    #定时模块
    import schedule 
    import time
    #引入schedule和time

    def job():
            a()
    #定义一个叫job的函数，函数的功能是打印'I'm working...'
    schedule.every(20).minutes.do(job)
    #schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
    #schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
    #schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
    #schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
    #schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

    while True:
        schedule.run_pending()
        time.sleep(1)    
    #15-17都是检查部署的情况，如果任务准备就绪，就开始执行任务。
a()    
go_time()
