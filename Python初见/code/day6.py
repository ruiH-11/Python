"""


"""

#函数多返回值
"""
def double_return():
    return 1,2

x, y = double_return()
print(x)
print(y)

#多种传参方式
#位置参数
def info(name,age,gander):
    print(name,age,gander)
info("zhang",123,"nan")

#关键字参数
info(name="zhang",age=123,gander="nan")
info("zhang",age=123,gander="nan")
#缺省参数（默认值）
def info(name,age,gander="nan"):
    print(name,age,gander)
info(name="were",age=333)
info("hehe",5458,"nv")
#位置不定长  (*args相当于生成一个元组来接受传入的数据)
def info(*args):
    print(args)
info(1, 2)
info(1, 2, 3, 4)
#关键字不定长(**args相当于一个字典)
def info(**kwargs):
    print(kwargs)
info(hh=45,dfs='dfs',df='jdhsf')
"""

#函数传参
def add(a,b):
    return a+b

def ans(add):
    print(add)

ans(add(1,2))