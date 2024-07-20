import os
import pandas as pd
 
path = 'E:/淘宝/名片模板/英文名片'
files= [ i for i in os.listdir(path)] #os.listdir返回指定目录下的所有文件和目录名

for file,i in zip(files,range(len(files))):
    old = path + '/' +file
    new = path + '/' +'CZ-'+str(i)
    print(old)
    print(new)
    os.rename(old,new)