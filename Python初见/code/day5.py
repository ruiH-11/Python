#数据容器的切片操作[起始:终止:步长]都为下标，取的元素是起始下标——终止下标-1

"""
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0:10:])

my_tuple = (1,2,3,4,5,6,7,8,9)
print(my_tuple[0:10:2])

my_str = '0123456789'
print(my_str[::2])
print(my_str[::-1]) #将序列反转，反向输出
print(my_str[9:0:-1])

#练习

my_str = '学大海河,来就,学大上'
print(my_str[::-1])
print(my_str[::-1].split(',')[2])
"""
"""
#4.  set 集合 无序的，不能用下标访问,每次打印都是乱序  允许修改  会去除重复元素
my_set = {"name","year","height","year"}
void_set = set()
print(void_set)
print(my_set)


# 添加元素 .add
my_set.add("money")
my_set.add("name")
print(my_set)

#移除元素 .remove
my_set.remove("year")
print(my_set)
    # ,pop 取出一个随机元素，集合里面去掉这个元素
my_set.pop()
print(my_set)

#清空集合  .clear
my_set.clear()
print(my_set)
"""

"""
#取两个集合的差集
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4}
c = a.difference(b)   #取a中有b中没有的形成新集合c，集合a b元素不变
print(c)
print(a)
print(b)

#消除两个集合的差集
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,4}
a.difference_update(b) #删除a中和b相同的元素，a会变，b不变
print(a)
print(b)

#两个集合合并
c = a.union(b)  #一个新集合，相同元素去重
print(c)

#len（）求长度
print(len(c))

#集合的遍历 不能用while 因为无法使用下标
i = None
for i in b:
    print(i)


#集合训练 信息去重

my_list = [1,2,3,3,5,6,4,5,1,4,2,5,1,1]
my_set = set()
for i in my_list:
    my_set.add(i)

print(my_set)
"""

"""
#5.字典 dict()   {key:value}  key值不能重复  value可以重复  无下标索引  但能通过key访问到对应的value值
            #如果key重复 取最后一个key：value                        return dict[kay] = value
void_dict = dict()  #或者 void_dict = {}
print(void_dict)
my_dict = {"name":"55","lahua":"54","wangwang":"325"}
print(my_dict)
print(my_dict["name"])

#嵌套字典
stu_score_dict = {
    "李华":{
        "数学":52,
        "语文":65,
        "英语":85
    }, "张强":{
        "数学":99,
        "语文":85,
        "英语":75,
    }
}
print(stu_score_dict)
print(stu_score_dict["张强"]["语文"])


#字典常用操作
#增加或更新元素
stu_score_dict["张超"]=dict()
stu_score_dict["张超"]["数学"]=52
stu_score_dict["张超"]["语文"]=52
stu_score_dict["张超"]["英语"]=52
print(stu_score_dict)
print(stu_score_dict["张超"])

stu_score_dict["张超"]["英语"]=99
print(stu_score_dict["张超"])

#.pop  取出value值并删除kay
a = stu_score_dict.pop("李华")
print(a)
print(stu_score_dict)

#.clear 清空字典

#.keys  获取全部key
print(stu_score_dict.keys())

#for循环遍历字典
i = None
for i in stu_score_dict.keys():
    print(f"名字是{i}")
    print(f"分数是{stu_score_dict[i]}")

#或者  for i in  stu_score_dict

#字典练习
staff = {"王力宏":{
            "部门":"科技部",
            "工资":3000,
            "级别":1,
            },"周杰伦":{
            "部门":"市场部",
            "工资":5000,
            "级别":2
            },"林俊杰":{
            "部门":"市场部",
            "工资":7000,
            "级别":3
            },"张学友":{
            "部门":"科技部",
            "工资":4000,
            "级别":1
            },"刘德华":{
            "部门":"市场部",
            "工资":6000,
            "级别":2
            }
         }
print(f"全体员工当前信息如下{staff}")
for i in staff:
    if staff[i]["级别"]==1:
        staff[i]["级别"]+=1
        staff[i]["工资"]+=1000

print(f"将级别为1的员工上升一级，工资加1000，操作后为：{staff}")
"""

#max()  和  min()  函数 根据ASCII表来  对于5种容器都适用



#容器转换：转列表list()，转元组tuple()，转字符串str()，转集合set()
#其中字典转列表元组和集合只保留key值，转字符串保留key和value



#容器排序函数 sorted()  排序后的结果都为列表,相当于转换为列表再排序
my_list = [5,6,2,5,1,9,8,1,3]
print(f"排序前{my_list}")
print(f"排序后的列表{sorted(my_list)}")

my_tuple = (5,6,2,5,1,9,8,1,3)
print(my_tuple)
print(sorted(my_tuple))

#降序排序
print(sorted(my_tuple,reverse=True))