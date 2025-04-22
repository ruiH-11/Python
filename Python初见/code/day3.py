#函数
#设计一个my_len()函数来返回字符串长度
"""
a = input("输入一个字符串：")
length = len(a)
print(length)

def my_len(date):
    count = 0
    for i in date:
        count += 1
    return count
print(my_len(a))
"""
#计算a+b
"""
def add(x,y):
    return x + y
a=int(input("输入两个数："))
b=int(input())
print(f"{a}+{b}={add(a,b)}")
"""

#自动查核酸
"""
def cha(temperture):
    if temperture <= 37.5 :
        print(f"欢迎！\n出示：\n体温监测中，体温是{temperture}度,正常，进入")
    else :
        print(f"欢迎！\n出示：\n体温监测中，体温是{temperture}度,隔离")


a=float(input("输入体温："))
cha(a)
"""

# 函数说明文档
def add(a,b):
    """
    add加法函数，传入两个参数，返回两数之和
    :param a:
    :param b:
    :return:
    """
    return a+b

#函数嵌套调用
"""
def say_hello():
    say_hai()
    print("hello")

def say_hai():
    print("hai")

say_hello()
say_hai()
"""
#在函数内部定义全局变量global()
"""
num=200
def a():
    print(num)
def b():
    global num
    num=500
    print(num)

a()
b()
print(num)
"""

#ATM模拟
"""
money = int(5000000)
name = None
a = None
def menu():
    print("---------主菜单----------")
    print(f"{name}，欢迎来到ATM")
    print("查询余额  [输入1]")
    print("存款     [输入2]")
    print("取款     [输入3]")
    print("退出     [输入4]")
    print("输入您的选择：")
    global a
    a = int(input())
    if a == 1:
        print("----------查询余额-----------")
        cha()
    elif a == 2:
        chun()
    elif a == 3:
        qu()
    elif a == 4:
        print("再见")
    else:
        a=4

def cha():

    print(f"{name}，您好，您的余额是{money}元")
def chun():
    print("----------存款-----------")
    b=int(input("输入要存多少钱："))
    global money
    money=b+money
    print(f"{name}，您好，您存款{b}元成功")
    cha()
def qu():
    print("----------取款-----------")
    c = int(input("输入要取多少钱："))
    global money
    money=money-c
    print(f"{name},您好，您取款{c}元成功")
    cha()

name = input("输入您的姓名：")
while True:
    menu()
    if a == 4:
        print("再见")
        break
"""