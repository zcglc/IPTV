# -*- coding: utf-8 -*-
import os , time
#设定文件路径
def a(path):
        i=1
        #对目录下的文件进行遍历
        for file in os.listdir(path):
        #判断是否是文件
                if os.path.isfile(os.path.join(path,file))==True:
                #设置新文件名
                        new_name=file.replace(file,"%d.jpg"%i)
                #重命名
                        os.rename(os.path.join(path,file),os.path.join(path,new_name))
                        i+=1
        #结束
        print ("End")
a(input('输入地址：'))
time.sleep(3)