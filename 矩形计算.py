import time,random

a=True
c=random.randint(0,32645683532453224574758758747687876665487322543257854695)
d=random.randint(0,84894988949848498489485954654484987948948987789779894878)
class Shoxian():
        def __init__(self,one,two):
            self.one=one
            self.two=two
        def chen(self):
            self.three=self.one*self.two
        def xians(self):
            self.chen()
            print('最终结果:%s'% self.three)


def choiced():
    print('------------------欢迎使用长方形面积计算公式系统-------------------')
    time.sleep(0.5)
    choice=int(input('请输入长(mm)：'))
    time.sleep(0.5)
    choice2=int(input('请输入宽(mm)：'))
    time.sleep(0.5)
    dfjk=Shoxian(choice,choice2)
    dfjk.xians()

def choiced2():
    chang=c
    kuang=d
    print('------------------欢迎使用长方形面积计算公式系统-------------------')
    time.sleep(0.5)
    print('系统已为您自动选择长：%s' % chang)
    time.sleep(0.5)
    print('系统已为您自动选择宽：%s' % kuang)
    time.sleep(0.5)
    dfjk=Shoxian(chang,kuang)
    dfjk.xians()

while a:    
    try:
        choiced()
    except:
        print('请输入数字!!!')
        time.sleep(0.5)
    b=input('请问是否还要继续，若要继续请按1，若要退出请按任意键：')
    time.sleep(0.5)
    if b=='1':
       print('程序已继续运行')
    else:
        a=False
        print('您已成功退出程序')
        