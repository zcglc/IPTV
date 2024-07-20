import time,random,re

shasho={'小海鸥':'我是一只海鸥，在蓝天下自由地翱翔，我将为你杀掉任何对象',
        '史莱姆':'虽然我的形象在游戏里表现欠佳，但是真正的我可是很强的',
        '小丽雅':'我的名字可能有些大众，不过我可不随众'}

print('欢迎使用魔鬼万金油有限公司智能下单系统')

def dianfei():
    a=True
    dizhi=input('请输入您的地址：')
    money=input('请输入您需要充值的能量：(月)')
    print('好的，为%s充值%s份的能量共需%s点数,您也可以使用等量的其他货币充值' % (dizhi,money,money))
    while a:
        chose=input('是否使用其他种类货币：')
        if chose=='是' or chose=='是的' or chose=='需要' or chose=='要使用':
            money_lei=input('请选择种类：灵魂 尖叫能量 灵晶 灵石')
            if money_lei=='灵魂' or money_lei=='尖叫能量' or money_lei=='灵晶' or money_lei=='灵石':
                print('好的，将从您的账户扣除%s份%s'%(money,money_lei))
                print('警告！！警告！！未检测到您账户下拥有余额')
                print('非常抱歉，此次不能为您服务')
                print('如有需要请再行联系')
                a=False                
            else:
                print('请准确输入货币名称')
        elif chose=='不要' or chose=='否' or chose=='不需要' or chose=='不用' or chose=='不使用':
            print('好的，将从您的账户扣除%s份%s'%(money,money_lei))
            print('警告！！警告！！未检测到您账户下拥有余额')
            print('非常抱歉，此次不能为您服务')
            print('如有需要再行联系')
            a=False                
        else:
            print('请回答是或否')
def mieko():
    a=True
    while a:
        print('欢迎使用抹杀程序，我们能为您提供各种抹杀服务（包括但不限于各种生物、模因、神灵、妹子、汉子、百合、基友）')
        xiao_name=input('请您输入需要抹杀对象的名称：')
        xiao_age=input('请您输入需要抹杀对象的年龄：')
        xiao_ardess=input('请您输入见到需抹杀对象的最后地点：')
        print('那么您需要抹杀%s的%s，最后出现在%s' % (xiao_age,xiao_name,xiao_ardess))
        print('好的，资料已上传，请稍候片刻等待杀手接单')
        time_wait=random.randint(1,20)
        for i in range(0,time_wait,1):
            print("\r等待接通中：%s秒！"% i, end="", flush=True)
            time.sleep(1)
        print("已接通")
        sha=str(random.sample(shasho.keys(),1))[2:-2]
        print('盯~~猛盯~~，杀手%s已接单\n杀手留语：%s' % (sha,str(shasho[sha])[2:]))
        print('渣滓，我是你这次雇佣的杀手，其他先不用谈，我们先来看看你出价几何')
        chujia=input('杀手先生要求您出价，那么您出价多少呢：\n（小提示：是按份数算的点数或能量）')
        shu=re.findall(r"\d+\.?\d*",chujia)
        if int(str(shu)[2:-2])>=30:
            print('%s：好，这个单接了，先转%s的定金给我' % (sha,'50%'))
            jiezhang=input('你要用什么结账')
            while a:                
                if jiezhang=='灵魂' or jiezhang=='尖叫能量' or jiezhang=='灵晶' or jiezhang=='灵石':
                    print('好，我直接从你的账户里扣除%s份的%s'% ((int(str(shu)[2:-2])/2),jiezhang))
                    print('等等，你他妈没钱，那在这糊弄鬼呢，滚犊子吧！！')
                    print('---------连接已断开----------')
                    print('不好意思，尊敬的客户，%s先生已离开，欢迎您的下次光临'%sha)
                    a=False
                else:
                    holai=input('请输入准确货币名称（你知道的）')
                    if holai=='灵魂' or holai=='尖叫能量' or holai=='灵晶' or holai=='灵石':
                        print('好，我直接从你的账户里扣除%s份的%s'% ((int(str(shu)[2:-2])/2),holai))
                        print('等等，你他妈没钱，那在这糊弄鬼呢，滚犊子吧！！')
                        print('---------连接已断开----------')
                        print('不好意思，尊敬的客户，%s先生已离开，欢迎您的下次光临'%sha)
                        a=False
        elif int(str(shu)[2:-2])<30:
            print('穷逼滚蛋，没钱别来买凶杀人')
            print('---------连接已断开----------')
            print('不好意思，尊敬的客户，%s先生已离开，欢迎您的下次光临'%sha)
            break
def yunshu():
    print('欢迎使用魔鬼公司快捷交通网')
    weizhi=input('请输入您需要去的位置')
    peson=input('请输入乘坐人数')
    print('前往地点：%s\n乘坐人数：%s人' % (weizhi,peson))

#def gmwq():
a=True

while a:
    one=input('请选择客服"01","02","03"')
    if one=='01':
        print('sorry,01号客服已被天堂的大天使长撬走了,暂时无人接替，已停止服务')
    elif one=='02':
        print('请于通讯法阵中输入02的编号寻找链接')
    elif one=='03':
        print('尊敬的客户您好，工号03号客服为您服务')
        while a:
            fuwu=input('请为您需要咨询什么服务\n①充能费  ②灭口  ③运输 ④购买武器 ⑤离开')
            if fuwu=='1' or fuwu=='充能费':
                dianfei()
            elif fuwu=='2' or fuwu=='灭口':
                mieko()
            elif fuwu=='3' or fuwu=='运输':
                yunshu()
            elif fuwu=='4' or fuwu=='购买武器':
                gmwq()
            elif fuwu=='5' or fuwu=='离开':
                print ('祝您生活愉快，魔鬼公司永远在您左右')
                exit()
            else:
                print('暂未开展其他服务，请期待后续更新')
            
    else:
        print('暂未研发其他客服')

