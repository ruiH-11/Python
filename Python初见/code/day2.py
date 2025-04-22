import random
"""
#比较运算符> <  ==  !=  <=  >=     True False
a = 1
b = 0
c = True
print(bool(a))
print(bool(b))
print(type(c))
print(a!=b)
"""

#if-else-elif 语句
"""
age = int(input("输入年龄："))
height = int(input("输入身高："))
if age >= 18:
    print(f"你成年了，需要买票10元")
elif height >= 180:
    print("你太高了，需要买票")
else:
    print(f"你还不够高，免费")
"""

"""
#猜数字  if嵌套

a = random.randint(1,10)
if a == int(input("输入第一次猜的数字：")) :
    print("对了")
if a == int(input("答案不对，第二次猜：")):
    print("对了")
elif a == int(input("还是不对，最后一次猜：")):
    print("对了")
else:
    print(f"都不对，数字是{a}")
"""
"""
#while 循环  1-100的累加
i = 1
sum = 0
while True:
    sum = sum + i
    i = i + 1
    if i == 100+1:
        break
print(sum)


#猜数字进阶
a = random.randint(1,100)
while True :
    b = int(input("猜一个数："))
    if b == a:
        print("猜对了")
        break
    if b > a:
        print("猜大了")
    if b < a:
        print("猜小了")
        
"""
"""
#打印九九乘法表  end=" " 不换行   \t制表符对齐
i = 1
while i<=9:
    j = 1
    while j <= i:
        print(f"{j}x{i}={i*j}\t",end='')
        j=j+1
    print("")#用于换行
    i = i+1
"""

"""
#for循环

for i in range(1,10):
    print(i,end="")

for i in "string":
    print(i,end="")

#for循环 1-100累加
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}x{i}={j*i}\t",end="")
    print("")
"""

#发工资模拟，continue break的应用
money = 20000
for i in range(1,21):
    b = random.randint(1,10)
    if b < 5:
        print(f"员工{i}的绩效为{b}，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}的绩效为{b}，发工资1000元，还剩{money}")
    else :
        print("钱不够了，不发了")
        break