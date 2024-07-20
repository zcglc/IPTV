import json,requests

headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
def fan():
    xx=input('主人请输入需要的内容哦：')
    data={'i':xx,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16046433394532',
    'sign': 'c38717fc3a291ab5b6c06058172f78d3',
    'lts': '1604643339453',
    'bv': 'acc97416ef67184f42e5a4a03c3d52ab',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'}
    fanyi=requests.post('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule',headers=headers,data=data)
    anwar=json.loads(fanyi.text)
    get=anwar['translateResult'][0][0]['tgt']
    print('主人的结果请收下：\n'+get)

def xunhuan():
    a=True
    fan()
    while a:
        b=input('主人还要继续吗，需要的话按‘1’，不需要的话按‘2’')
        if b=='2':
            a=False
            print('期待主人的下次使用')
        elif b=='1':
            print('翻译姬继续工作中-------')
            fan()

xunhuan()
