#数据容器
#  1.list列表及其基本方法
#定义列表
"""
name_list=['hh','shd']
print(name_list)
print(name_list[0][0])
print(type(name_list))

a=[[1,2,3],[4,5,6]]

#列表下标索引.
# 从前向后0-n
# 从后向前 -1——>-n+1   -1表示最后一位数
print(a[0])
print(a[0][2])
print(a[0][-1])
#string类似列表
b="string"
print(b[2])
"""
"""
#方法 class类似函数
#列表的方法
a=[[1,2,3],[4,5,6]]
#1  .index  查找元素下标，
b=a.index([4,5,6])
print(b)
a[1]=[7,8,9]
print(a)
#2   .insret,插入,后面元素后移
a.insert(1,[10,11,12])
print(f"插入后位置1:{a}")
#3  .append 尾部追加单个元素
a.append([13,14,15])
print(f"尾部追加后：{a}")
#4   .extend 尾部追加一组元素,不能追加一个元素为列表的元素
a.extend([16,17,18])
print(a)

#5   删除元素  del  直接删除
#6     .pop，取出来，再删除
del a[5]
print(f"删除第六个元素后{a}")
b = a.pop(0)
print(f"删除第一个元素后{a}")
print(f"将第一个元素传给b：{b}")

#7     .remove,从前向后搜索第一个值然后删除
a.remove(18)
print(f"通过remove函数删除一个名为18的元素后{a}")


#8      .count统计列表中某个的元素的数量
c=a.count(16)
print(f"a中的元素为16的个数为{c}")

#9     len函数可以统计出列表中的总的元素个数
print(f"a中的元素个数为：{len(a)}")

#10    .clear直接删除整个列表
a.clear()
print(f"清空后的列表{a}")
"""

#列表练习
"""
a=[21,25,21,23,22,20]
a.append(31)
a.extend([29,33,30])
b=a.pop(0)
c=a.pop(-1)
d=a.index(31)
print(f"取出的第一个元素为{b}，取出最后一个元素为{c}，元素'31'的下标为{d}")"""


#列表的遍历，while for
"""
my_list=[1,2,3,4,5,6,7,8,9,10]
i = 1
while i<len(my_list):
    print(my_list[i])
    i+=2


for j in my_list:
    if j%2==0:
        print(j)
"""
"""
#2.元组(tuple),不能修改的列表
t1 =(1,2,3,4,5,6,7,8,9,10)
#空元组
t2 = ()
t3 = tuple()
#单元素元组后要加一个逗号
t4 = (1,)
#元组嵌套
t5 = ((1,2,3),(4,5,6),(7,8,9))

print(t5[1][1])

#index count  len  操作与列表list相同
i = 0
while i<len(t1):
    print(t1[i],end=" ")
    i+=1

for j in t1:
    print(j)

#元组练习
t_1=('周杰伦',11,['football','music'])
a=t_1.index(11)
print(f"年龄下标为{a}")
print(t_1[0])
t_1[2].remove("football")
t_1[2].insert(0,"coding")
print(t_1)
"""

#字符串string,不可修改，改动的话只能变成一个新的字符串
"""
my_name = 'huang 123 ru'
#下标索引取值
print(my_name[0])
print(my_name[-1])
#index方法，查找某元素的下标
print(my_name.index("123"))
print(my_name.index("12"))

#replace方法  替换某一部分形成一个新的字符串
my_name1=my_name.replace("huang","yang")
print(my_name)
print(f"替换后的字符串{my_name1}")

#split方法  分割
my_str='1 2 3 4 5'
my_str_list=my_str.split(' ')
print(my_str_list)

#strip方法   规整操作
#.strip('参数')    在字符串首尾删除所给的参数 参数一个一个检测
new_my_name=my_name.strip('hi')
print(new_my_name)
#统计字符串中某个字符串的出现次数 .count
print(my_str.count('3'))

#统计字符串的长度len()
print(len(my_name))
"""

#字符串练习
"""
my_str="itheima itcast boxuegu"

print(f"字符串{my_str}中有{my_str.count("it")}个it字符")
print(f"字符串{my_str}中空格被替换后为{my_str.replace(" ","|")}")
print(f"字符串{my_str.replace(" ","|")}按照|分割后得到{my_str.replace(" ","|").split("|")}")
"""

