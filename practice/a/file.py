#练习文件操作
import requests
import json

def getContent():
   print("开始发起请求")
   res =  requests.get("https://apis.tianapi.com/fairytales/index?key=0b03fd31cd024342a56bb161c3ad086&id=352fe25daf686bdb")
   print("请求结束")
   data = res.text
   try:
      with open("data1.json","w",encoding="utf-8") as fs:
           fs.write(data)
   except IOError as e:
      print(e)
   print("保存成功")

def save():
   print("开始发起请求")
   res =  requests.get("https://apis.tianapi.com/fairytales/index?key=0b03fd31cd024342a56bb161c3ad086&id=352fe25daf686bdb")
   print("请求结束")
   data =json.loads(res.text)
   print(data)
   try:
      with open("data2.json","w") as fs:
           json.dump(data,fs,ensure_ascii=False)
   except IOError as e:
      print(e)
   print("保存成功")

def test():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs,ensure_ascii=False)
    except IOError as e:
        print(e)
    print('保存数据完成!')

def main():
   # getContent()
   #  test()
   save()

if __name__=='__main__':
   main()