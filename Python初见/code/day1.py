# 666整数
# 12.12浮点数
# 'whoo001'字符串
"""
print(666)
print(12.12)
print('whoo001')
"""


"""
# 变量
a = input()
b = input()
print(a+b)
print(type(a+b))
print(int(a)+int(b))
print(type(int(a)+int(b)))
print(int(a)-10)"""

"""
money = 50
#购买一个冰淇淋15元
money = money-15
print("还剩",money,"元")
#再购买一个雪糕10元
money = money-10
print("还剩",money,"元")"""

"""
#算数运算符
print("1 + 1 =",1+1)
print("2 - 1 =",2-1)
print("2 * 2 =",2*2)
print("4 / 2 =",4/2)
print("11 // 3  =",11//3)  # 整除
print("9 % 2 =",9%2)
print("2 ** 3 =",2**3)     # n**m n的m次方
"""

"""
#赋值运算符(算数运算符+"="）
age = 18

#字符串内本就有引号
name_1 = "'zhangsan'"   #包含单引号
name_2 = '"chengyuan"'  #包含双引号
print(name_1)
print(name_2)

#转义字符
name_3 = "\"lisi\""
print(name_3)
"""
"""
#字符串占位拼接%s  %d   %f
name = "zhangsan"
phone = 123456789
print("姓名："+name+" 电话号码:%d" % phone)
age = 18
height = 180
print("年龄：%d 身高：%f" % (age,height))
"""

"""
#数字精度设置%n.md,%n.mf  n位宽度，m位小数点后位数
a = 153.253
print("%6.2f" % a)
print("%15f" % a)
print("%.2f" % a)
"""
"""
#f"{变量} {变量}"快速格式化
name = "zhangsan"
phone = 123456789
age = 18
height = 180
print(f"名字“{name} 电话号码：{phone} 年龄:{age} 身高：{height}")
"""


#输入语句 input
age = int(input("输入一个数："))
print("输入的数是：%d"%age)





